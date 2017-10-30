def sum_ind(a, b):
    return 1 - (1 - a) * (1 - b)


def get_probs(groups):
    probs = {}
    for group in groups:
        size = len(group.cells)
        for cell in group.cells:
            prob = group.w / size
            if cell in probs:
                probs[cell] = sum_ind(probs[cell], prob)
            else:
                probs[cell] = prob

    return probs


def print_probs(probs, field, m, n):
    for i in range(m):
        for j in range(n):
            if (i, j) in probs:
                print('{0:6.2f}'.format(probs[(i, j)]), end='')
            else:
                print('{0:6d}'.format(field[i][j]), end='')

        print('\n', end='')
