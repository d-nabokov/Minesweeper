def sum_ind(a, b):
    return 1 - (1 - a) * (1 - b)


def get_probs(groups):
    probs = {}
    for group in groups:
        size = len(group.cells)
        print("size", size)
        for cell in group.cells:
            prob = group.w / size
            print("prob", prob)
            if cell in probs:
                probs[cell] = sum_ind(probs[cell], prob)
            else:
                probs[cell] = prob

    print(probs)
