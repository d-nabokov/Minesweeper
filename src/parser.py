from src import config as conf
from src.game import Game
from src.group import Group


class ParseException(Exception):
    def __init__(self, msg):
        self.msg = msg


class ErrorMessages:
    PROPERTIES = 'First line should contain 3 numbers with separators'
    NEGATIVE_PROPERTIES = 'Numbers must be more that 0'
    SHORT_ROW = 'Row is too short, should be {} values'
    LOW_CORRECTED_WEIGHT = 'Number of mines in area {} is more that weight of cell'
    UNKNOWN_SYMBOL = 'Unknown symbol "{}"'
    WEIGHT_BOUNDS = 'Digital cell should have weight in [1, 8], actual {}'


def __create_group(field, area, w):
    cells = set()
    for i, j in area:
        if field[i][j] == conf.UNOPENED_CELL:
            cells.add((i, j))
        elif field[i][j] == conf.MINE:
            w -= 1

    if w < 0:
        raise ParseException(ErrorMessages.LOW_CORRECTED_WEIGHT.format(sorted(area)))

    return Group(cells, w) if len(cells) > 0 else None


def get_area(x, y, m, n):
    area = []
    if x < 0 or y < 0 or x >= m or y >= n:
        return area

    for i in range(max(0, x - 1), min(m - 1, x + 1) + 1):
        for j in range(max(0, y - 1), min(n - 1, y + 1) + 1):
            if i == x and j == y:
                continue
            area.append((i, j))

    return area


def __get_groups(field, m, n):
    groups = []
    for i in range(m):
        for j in range(n):
            if field[i][j] > 0:
                g = __create_group(field, get_area(i, j, m, n), field[i][j])
                if g is not None:
                    groups.append(g)

    return groups


def parse_field(filename):
    with open(filename, 'rt') as fin:
        properties = fin.readline().strip().split(conf.SEP)
        if len(properties) != 3:
            raise ParseException(ErrorMessages.PROPERTIES)
        try:
            m, n, mines = map(lambda x: int(x), properties)
        except ValueError:
            raise ParseException(ErrorMessages.PROPERTIES)

        if m <= 0 or n <= 0 or mines <= 0:
            raise ParseException(ErrorMessages.NEGATIVE_PROPERTIES)

        field = [None] * m
        for i in range(m):
            field[i] = [conf.UNOPENED_CELL] * n
        for i in range(m):
            cells = fin.readline().strip().split(conf.SEP, n - 1)
            if len(cells) != n:
                raise ParseException(ErrorMessages.SHORT_ROW.format(n))
            for j in range(n):
                cell = cells[j]
                if cell == conf.UNOPENED_CELL_STR:
                    continue
                elif cell == conf.EMPTY_CELL_STR:
                    field[i][j] = conf.EMPTY_CELL
                elif cell == conf.MINE_STR:
                    field[i][j] = conf.MINE
                elif cell.isdecimal():
                    # negative values are not decimal, so weight >= 0
                    weight = int(cell)
                    if weight < 1 or weight > 8:
                        raise ParseException(ErrorMessages.WEIGHT_BOUNDS.format(weight))
                    field[i][j] = weight
                else:
                    raise ParseException(ErrorMessages.UNKNOWN_SYMBOL.format(cell))

        return field, m, n, mines


def parse_game(filename):
    field, m, n, mines = parse_field(filename)
    groups = __get_groups(field, m, n)
    return Game(field, m, n, groups, mines)
