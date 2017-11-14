from src import config as conf
from src.game import Game
from src.group import Group


def __create_group(field, area, w):
    cells = set()
    for i, j in area:
        if field[i][j] == conf.UNOPENED_CELL:
            cells.add((i, j))
        elif field[i][j] == conf.MINE:
            w -= 1
        # TODO remove?
        elif field[i][j] == conf.EMPTY_CELL:
            continue

    # TODO check w for >= 0

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
        first_line = fin.readline()
        m, n, mines = map(lambda x: int(x), first_line.strip().split(conf.SEP))
        # TODO check if ok
        field = [None] * m
        for i in range(m):
            field[i] = [conf.UNOPENED_CELL] * n
        for i in range(m):
            cells = fin.readline().strip().split(conf.SEP, n)
            # TODO check size
            for j in range(n):
                cell = cells[j]
                if cell == conf.UNOPENED_CELL_STR:
                    continue
                elif cell == conf.EMPTY_CELL_STR:
                    field[i][j] = conf.EMPTY_CELL
                elif cell == conf.MINE_STR:
                    field[i][j] = conf.MINE
                elif cell.isdecimal():
                    num = int(cell)
                    # TODO check 1-8
                    field[i][j] = num
                # TODO add mines_left

    return field, m, n, mines


def parse_game(filename):
    field, m, n, mines = parse_field(filename)
    groups = __get_groups(field, m, n)
    return Game(field, m, n, groups, mines)
