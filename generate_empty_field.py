import sys

from src import config


def main():
    if len(sys.argv) < 4:
        print('Use "python generate_empty_field.py <height> <width> <number_of_mines> [<file>=\'field\']"')
        return

    try:
        m, n, mines = map(lambda x: int(x), sys.argv[1:4])
    except ValueError:
        print('height, width and number_of_mines should be digital')
        return

    if m <= 0 or n <= 0 or mines < 0:
        print('height, width and number_of_mines should be positive')
        return

    file = sys.argv[4] if len(sys.argv) > 4 else 'field'

    with open(file, 'wt') as fout:
        print(m, n, mines, sep=config.SEP, file=fout)
        for _ in range(m):
            print(config.SEP.join([config.UNOPENED_CELL_STR] * n), file=fout)


if __name__ == '__main__':
    main()
