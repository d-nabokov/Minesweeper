import src.groups_solver as groups_solver
import src.parser as parser


def solve(input_file, output_file):
    game = parser.parse_game(input_file)
    with open(output_file, 'wt') as fout:
        mines, not_mines = groups_solver.solve(game.groups)
        if mines and not_mines:
            print('1', file=fout)
            for x, y in mines:
                print(x, y, file=fout)

            print('-', file=fout)
            for x, y in not_mines:
                print(x, y, file=fout)
