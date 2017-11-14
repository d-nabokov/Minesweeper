import unittest

from src import parser
from src import config as conf
from src.group import Group


class ParserTest(unittest.TestCase):
    def test_get_area(self):
        first = [(0, 1), (1, 0), (1, 1)]
        self.assertEqual(first, parser.get_area(0, 0, 4, 3))

        second = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
        self.assertEqual(second, parser.get_area(0, 1, 4, 3))

        third = [(2, 1), (2, 2), (3, 1)]
        self.assertEqual(third, parser.get_area(3, 2, 4, 3))

    def test_parse(self):
        field, m, n, _ = parser.parse_field('inputs/001')
        self.assertEqual(4, m)
        self.assertEqual(3, n)

        self.assertEqual(4, field[1][1])
        self.assertEqual(3, field[2][1])

        for i in (0, 3):
            for j in range(3):
                self.assertEqual(conf.UNOPENED_CELL, field[i][j])

        for i in (1, 2):
            for j in (0, 2):
                self.assertEqual(conf.UNOPENED_CELL, field[i][j])

    def test_get_groups(self):
        expected = [
            Group({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)}, 4),
            Group({(1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)}, 3)
        ]

        groups = parser.parse_game('inputs/001').groups
        self.assertEqual(expected, groups)

    def test_get_groups_with_mines(self):
        expected = [
            Group({(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 2)}, 3),
            Group({(1, 0), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)}, 2)
        ]

        groups = parser.parse_game('inputs/002').groups
        self.assertEqual(expected, groups)

    def test_ignore_groups_without_unopened_cells(self):
        groups = parser.parse_game('inputs/004').groups

        self.assertEqual(7, len(groups))

    def test_ignore_empty_cells(self):
        expected_first_five = [
            Group({(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}, 3),
            Group({(0, 1), (0, 2), (0, 3)}, 2),
            Group({(0, 2), (0, 3), (0, 4)}, 2),
            Group({(0, 3), (0, 4), (0, 5)}, 1),
            Group({(0, 4), (0, 5), (0, 6), (1, 6), (2, 6)}, 3),
        ]

        groups = parser.parse_game('inputs/005').groups
        self.assertEqual(expected_first_five, groups[0:5])
