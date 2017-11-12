import unittest

import GroupSolver
import Parser
from Group import Group


class GroupSolverTest(unittest.TestCase):
    def test_equal_groups(self):
        g = Group({1, 2, 3}, 2)
        groups = [g, g]
        GroupSolver.operate_groups(groups)

        self.assertEqual(1, len(groups))
        self.assertEqual(g, groups[0])

    def test_subgroup(self):
        g1 = Group({1, 2}, 1)
        g2 = Group({1, 2, 3}, 1)
        groups = [g1, g2]
        GroupSolver.operate_groups(groups)

        self.assertEqual(2, len(groups))

        group = groups[0]
        self.assertEqual(1, group.w)
        self.assertEqual({1, 2}, group.cells)

        group = groups[1]
        self.assertEqual(0, group.w)
        self.assertEqual({3}, group.cells)

    def test_intersection(self):
        g1 = Group({1, 2, 3}, 1)
        g2 = Group({2, 3, 4, 5}, 3)
        groups = [g1, g2]
        GroupSolver.operate_groups(groups)

        self.assertEqual(3, len(groups))

        group = groups[0]
        self.assertEqual(0, group.w)
        self.assertEqual({1}, group.cells)

        group = groups[1]
        self.assertEqual(2, group.w)
        self.assertEqual({4, 5}, group.cells)

        group = groups[2]
        self.assertEqual(1, group.w)
        self.assertEqual({2, 3}, group.cells)

    def test_get_cells(self):
        g1 = Group({1, 2, 3}, 3)
        g2 = Group({4, 5}, 1)
        g3 = Group({5, 6}, 0)
        g4 = Group({7, 8, 9}, 2)

        mines, not_mines = GroupSolver.get_reliable_cells([g1, g2, g3, g4])

        self.assertEqual(3, len(mines))
        self.assertEqual(g1.cells, mines)

        self.assertEqual(2, len(not_mines))
        self.assertEqual(g3.cells, not_mines)

    def test_simple_solve(self):
        groups = Parser.parse_game('inputs/003').groups
        mines, not_mines = GroupSolver.solve(groups)

        self.assertEqual(0, len(mines))
        self.assertEqual({(2, 1)}, not_mines)

    def test_no_reliable_solution(self):
        groups = Parser.parse_game('inputs/004').groups
        mines, not_mines = GroupSolver.solve(groups)

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

        groups = Parser.parse_game('inputs/005').groups
        mines, not_mines = GroupSolver.solve(groups)

        self.assertEqual(mines_expected, mines)
        self.assertEqual(not_mines_expected, not_mines)
