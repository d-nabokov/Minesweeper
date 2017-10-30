def sum_ind(a, b):
    return 1 - (1 - a) * (1 - b)


def get_probs(groups):
    probs = {}
    for group in groups:
        for cell in group.cells:
            prob = group.w / group.size()
            if cell in probs:
                probs[cell] = sum_ind(probs[cell], prob)
            else:
                probs[cell] = prob

    return probs


def print_probs(probs, game):
    for i in range(game.m):
        for j in range(game.n):
            if (i, j) in probs:
                print('{0:6.2f}'.format(probs[(i, j)]), end='')
            else:
                print('{0:6d}'.format(game.field[i][j]), end='')

        print('\n', end='')
