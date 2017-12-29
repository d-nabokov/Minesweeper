import sys

import re

from src import config as conf
from src.parser import parse_game, ParseException


def convert(val):
    if 1 <= val <= 8:
        return str(val)
    elif val == conf.EMPTY_CELL:
        return conf.EMPTY_CELL_STR
    elif val == conf.UNOPENED_CELL:
        return conf.UNOPENED_CELL_STR
    elif val == conf.MINE:
        return conf.MINE_STR


def do_mark(game, lines, output):
    f = game.field
    p = re.compile('(^(?P<i>\d+) (?P<j>\d+)\s*$)|(?P<sep>^-\s*$)')
    for line in lines:
        m = p.fullmatch(line)
        if m.group('sep'):
            break
        else:
            i = int(m.group('i'))
            j = int(m.group('j'))
            f[i][j] = conf.MINE

    with open(output, 'wt') as fout:
        print(game.m, game.n, game.mines, sep=conf.SEP, file=fout)
        for row in f:
            print(conf.SEP.join(convert(val) for val in row), file=fout)


def main():
    if len(sys.argv) < 3:
        print('Use "python mark_mines.py <game_file> <list_file> [<output_file>=<game_file>]"')
        return

    output = sys.argv[3] if len(sys.argv) > 3 else sys.argv[1]

    try:
        game = parse_game(sys.argv[1])
    except ParseException as e:
        print(e.msg)
        return

    with open(sys.argv[2], 'rt') as list_file:
        lines = list_file.readlines()
        if not lines:
            return
        if re.search('^\d+ \d+\t0\.\d+\s*$', lines[0]):
            print('No reliable solution, try a guess')
            return

        elif re.search('(^\d+ \d+\s*$)|(^-\s*$)', lines[0]):
            do_mark(game, lines, output)

        else:
            print('Invalid file format')


if __name__ == '__main__':
    main()
