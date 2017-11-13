import sys

from src.solver import solve


def main():
    argc = len(sys.argv)
    if argc < 2:
        print('Use "python minesweeper.py <input filename> [<output filename>]"')
        return 
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if argc > 2 else 'out'
    try:
        solve(input_file, output_file)
    except FileNotFoundError:
        print('No such file')
        return


if __name__ == '__main__':
    main()
