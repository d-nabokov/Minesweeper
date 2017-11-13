import filecmp
import unittest

import os

import solver


class GroupSolverTest(unittest.TestCase):
    TEST_FILE = 'tmp'

    def test_test(self):
        solver.solve('inputs/001', GroupSolverTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/001', GroupSolverTest.TEST_FILE, shallow=False))

        solver.solve('inputs/002', GroupSolverTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/002', GroupSolverTest.TEST_FILE, shallow=False))

        solver.solve('inputs/003', GroupSolverTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/003', GroupSolverTest.TEST_FILE, shallow=False))

        solver.solve('inputs/004', GroupSolverTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/004', GroupSolverTest.TEST_FILE, shallow=False))

        solver.solve('inputs/005', GroupSolverTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/005', GroupSolverTest.TEST_FILE, shallow=False))

    def tearDown(self):
        os.remove(GroupSolverTest.TEST_FILE)
