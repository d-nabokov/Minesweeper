import filecmp
import unittest

import os

from src.solver import solve


class FunctionalTests(unittest.TestCase):
    TEST_FILE = 'tmp'

    def test_test(self):
        solve('inputs/001', FunctionalTests.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/001', FunctionalTests.TEST_FILE, shallow=False))

        solve('inputs/002', FunctionalTests.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/002', FunctionalTests.TEST_FILE, shallow=False))

        solve('inputs/003', FunctionalTests.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/003', FunctionalTests.TEST_FILE, shallow=False))

        solve('inputs/004', FunctionalTests.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/004', FunctionalTests.TEST_FILE, shallow=False))

        solve('inputs/005', FunctionalTests.TEST_FILE)
        self.assertTrue(filecmp.cmp('outputs/005', FunctionalTests.TEST_FILE, shallow=False))

    def tearDown(self):
        os.remove(FunctionalTests.TEST_FILE)
