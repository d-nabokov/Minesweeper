import src.probabilities as probabilities
import src.groups_solver as groups_solver
import src.parser as parser


def solve(input_file, output_file):
    game = parser.parse_game(input_file)
    with open(output_file, 'wt') as fout:
        mines, not_mines = groups_solver.solve(game.groups)
        if mines or not_mines:
            for x, y in mines:
                print(x, y, file=fout)

            print('-', file=fout)
            for x, y in not_mines:
                print(x, y, file=fout)
        else:
            probs = probabilities.get_probs(game.groups)
            # sort first by probability, then by cell (for lexicographical order)
            sorted_probs = sorted(probs.items(), key=lambda prob: (prob[1], prob[0]))
            for cell, p in sorted_probs:
                x, y = cell
                print("{0} {1}\t{2:.2f}".format(x, y, p), file=fout)
