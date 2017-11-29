import unittest

from src import groups_solver
from src.group import Group
from src.groups_solver import SolveException
from src.parser import parse_game


class GroupsSolverTest(unittest.TestCase):
    def test_equal_groups(self):
        g = Group({1, 2, 3}, 2)
        groups = [g, g]
        groups_solver.operate_groups(groups)

        self.assertEqual(1, len(groups))
        self.assertEqual(g, groups[0])

    def test_subgroup(self):
        g1 = Group({1, 2}, 1)
        g2 = Group({1, 2, 3}, 1)
        groups = [g1, g2]
        groups_solver.operate_groups(groups)

        self.assertEqual(2, len(groups))

        self.assertEqual(Group({1, 2}, 1), groups[0])

        self.assertEqual(Group({3}, 0), groups[1])

    def test_intersection(self):
        g1 = Group({1, 2, 3}, 1)
        g2 = Group({2, 3, 4, 5}, 3)
        groups = [g1, g2]
        groups_solver.operate_groups(groups)

        self.assertEqual(3, len(groups))

        self.assertEqual(Group({1}, 0), groups[0])

        self.assertEqual(Group({4, 5}, 2), groups[1])

        self.assertEqual(Group({2, 3}, 1), groups[2])

    def test_get_cells(self):
        g1 = Group({1, 2, 3}, 3)
        g2 = Group({4, 5}, 1)
        g3 = Group({5, 6}, 0)
        g4 = Group({7, 8, 9}, 2)

        mines, not_mines = groups_solver.get_reliable_cells([g1, g2, g3, g4])

        self.assertEqual(3, len(mines))
        self.assertEqual(g1.cells, mines)

        self.assertEqual(2, len(not_mines))
        self.assertEqual(g3.cells, not_mines)

    def test_simple_solve(self):
        groups = parse_game('inputs/003').groups
        mines, not_mines = groups_solver.solve(groups)

        self.assertEqual(0, len(mines))
        self.assertEqual({(2, 1)}, not_mines)

    def test_no_reliable_solution(self):
        groups = parse_game('inputs/004').groups
        mines, not_mines = groups_solver.solve(groups)

        self.assertEqual(0, len(mines))
        self.assertEqual(0, len(not_mines))

    def test_solve(self):
        mines_expected = {
            (0, 1),
            (0, 2),
            (0, 4),
            (0, 6),
            (4, 5),
            (6, 0),
            (7, 4)
        }

        not_mines_expected = {
            (0, 0),
            (0, 3),
            (0, 5),
            (3, 0),
            (3, 6),
            (5, 5),
            (6, 5),
            (7, 5)
        }

        groups = parse_game('inputs/005').groups
        mines, not_mines = groups_solver.solve(groups)

        self.assertEqual(mines_expected, mines)
        self.assertEqual(not_mines_expected, not_mines)

    def test_conflict(self):
        groups = parse_game('invalid_inputs/conflict_cells').groups
        with self.assertRaises(SolveException):
            groups_solver.solve(groups)
