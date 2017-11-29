import filecmp
import unittest

import os

from src.solver import solve


class FunctionalTest(unittest.TestCase):
    TEST_FILE = 'tmp'

    def test_correct_program_output(self):
        solve('inputs/000', FunctionalTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/000', FunctionalTest.TEST_FILE, shallow=False))

        solve('inputs/001', FunctionalTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/001', FunctionalTest.TEST_FILE, shallow=False))

        solve('inputs/002', FunctionalTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/002', FunctionalTest.TEST_FILE, shallow=False))

        solve('inputs/003', FunctionalTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/003', FunctionalTest.TEST_FILE, shallow=False))

        solve('inputs/004', FunctionalTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/004', FunctionalTest.TEST_FILE, shallow=False))

        solve('inputs/005', FunctionalTest.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/005', FunctionalTest.TEST_FILE, shallow=False))

    def tearDown(self):
        if os.path.isfile(self.TEST_FILE):
            os.remove(self.TEST_FILE)
