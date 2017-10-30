import Config


def sum_ind(a, b):
    return 1 - (1 - a) * (1 - b)


def get_raw_probs(groups):
    probs = {}
    for group in groups:
        for cell in group.cells:
            prob = group.w / group.size()
            if cell in probs:
                probs[cell] = sum_ind(probs[cell], prob)
            else:
                probs[cell] = prob

    return probs


def correct_probs(probs, groups):
    cycles = 0
    while True:
        cycles += 1
        changed = False
        for group in groups:
            s = sum(probs[cell] for cell in group.cells)
            print('diff: {}, sum = {}, expected {}'.format(abs(s - group.w), s, group.w))
            if not abs(s - group.w) < Config.DELTA:
                changed = True
                k = group.w / s
                for cell in group.cells:
                    probs[cell] *= k

        if not changed:
            break

        print('*************')

    print('algorithm did {} cycles for {} groups'.format(cycles, len(groups)))


def get_probs(game):
    probs = get_raw_probs(game.groups)
    correct_probs(probs, game.groups)
    return probs


def print_probs(probs, game):
    for i in range(game.m):
        for j in range(game.n):
            if (i, j) in probs:
                print('{0:6.2f}'.format(probs[(i, j)]), end='')
            else:
                if game.field[i][j] > 0:
                    print('{0:3d}(с)'.format(game.field[i][j]), end='')
                else:
                    print('{0:>6}'.format(Config.EMPTY_CELL_STR), end='')

        print('\n', end='')
