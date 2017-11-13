import src.config as config


def __sum_ind(a, b):
    return 1 - (1 - a) * (1 - b)


def get_raw_probs(groups):
    probs = {}
    for group in groups:
        for cell in group.cells:
            prob = group.w / group.size()
            if cell in probs:
                probs[cell] = __sum_ind(probs[cell], prob)
            else:
                probs[cell] = prob

    return probs


def correct_probs(probs, groups):
    while True:
        changed = False
        for group in groups:
            s = sum(probs[cell] for cell in group.cells)
            if not abs(s - group.w) < config.EPS:
                changed = True
                k = group.w / s
                for cell in group.cells:
                    probs[cell] *= k

        if not changed:
            break


def get_probs(groups):
    probs = get_raw_probs(groups)
    correct_probs(probs, groups)
    return probs


def print_probs(probs, game):
    for i in range(game.m):
        for j in range(game.n):
            if (i, j) in probs:
                print('{0:6.2f}'.format(probs[(i, j)]), end='')
            else:
                cell = game.field[i][j]
                if cell > 0:
                    print('{0:3d}(d)'.format(game.field[i][j]), end='')
                elif cell == config.UNOPENED_CELL:
                    print('{0:>6}'.format(config.UNOPENED_CELL_STR), end='')
                elif cell == config.MINE:
                    print('{0:>6}'.format(config.MINE_STR), end='')

        print('\n', end='')
