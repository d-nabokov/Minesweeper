from src import groups_solver
from src.parser import parse_game
from src.probabilities import get_probs


def solve(input_file, output_file):
    game = parse_game(input_file)
    with open(output_file, 'wt') as fout:
        mines, not_mines = groups_solver.solve(game.groups)
        if mines or not_mines:
            for x, y in sorted(mines):
                print(x, y, file=fout)

            print('-', file=fout)
            for x, y in sorted(not_mines):
                print(x, y, file=fout)
        else:
            probs = get_probs(game.groups)
            # sort first by probability, then by cell (for lexicographical order)
            sorted_probs = sorted(probs.items(), key=lambda prob: (prob[1], prob[0]))
            for cell, p in sorted_probs:
                x, y = cell
                print("{0} {1}\t{2:.2f}".format(x, y, p), file=fout)
