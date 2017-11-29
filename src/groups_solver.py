from src.group import Group


class SolveException(Exception):
    def __init__(self, msg):
        self.msg = msg


def operate_groups(groups):
    result = False

    size = len(groups)
    i = 0
    while i < size - 1:
        j = i
        while j + 1 < size:
            j += 1
            g1, g2 = groups[i], groups[j]

            if g1.cells == g2.cells:
                if g1.w == g2.w:
                    del groups[i]
                    j -= 1
                    size -= 1
                    result = True
                    continue
                else:
                    raise SolveException('Conflict in groups, check cells near {}'.format(g1.cells))

            parent, child = (g1, g2) if len(g1.cells) >= len(g2.cells) else (g2, g1)
            if parent.cells >= child.cells:
                parent.subtract(child)
                result = True
                continue

            parent, child = (g1, g2) if g1.w >= g2.w else (g2, g1)
            intersection = parent.cells & child.cells
            if intersection and parent.w - child.w == len(parent.cells) - len(intersection):
                new_group = Group(intersection, child.w)
                parent.subtract(new_group)
                child.subtract(new_group)
                groups.append(new_group)
                result = True
                continue

        i += 1

    return result


def get_reliable_cells(groups):
    mines = set()
    not_mines = set()
    for group in groups:
        if group.all_mines():
            mines |= group.cells
        elif group.all_not_mines():
            not_mines |= group.cells

    return mines, not_mines


def solve(groups):
    while True:
        changed = operate_groups(groups)
        if not changed:
            break

    return get_reliable_cells(groups)
