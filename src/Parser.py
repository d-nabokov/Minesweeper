from Group import Group

EMPTY_CELL_STR = '#'
EMPTY_CELL = -1

SEP = ' '


def create_group(field, area, w):
    cells = set()
    for i, j in area:
        if field[i][j] == EMPTY_CELL:
            cells.add((i, j))
        # TODO subtract weight

    return Group(cells, w)


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


def get_groups(field, m, n):
    groups = []
    for i in range(m):
        for j in range(n):
            if field[i][j] > 0:
                g = create_group(field, get_area(i, j, m, n), field[i][j])
                groups.append(g)

    return groups


def parse_field(filename):
    with open(filename, 'rt') as fin:
        first_line = fin.readline()
        m, n, mines = map(lambda x: int(x), first_line.strip().split(SEP))
        # TODO check if ok
        field = [None] * m
        for i in range(m):
            field[i] = [EMPTY_CELL] * n
        for i in range(m):
            cells = fin.readline().strip().split(SEP, n)
            # TODO check size
            for j in range(n):
                cell = cells[j]
                if cell == EMPTY_CELL_STR:
                    continue
                elif cell.isdecimal():
                    num = int(cell)
                    # TODO check 1-8
                    field[i][j] = num
                # TODO check flags, add mines_left

    return field, m, n, mines


def parse_groups(filename):
    field, m, n, _ = parse_field(filename)
    return get_groups(field, m, n)
