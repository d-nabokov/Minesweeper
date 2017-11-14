import unittest

import os

from src.parser import ParseException, ErrorMessages
from src.solver import solve


class ValidateInputTest(unittest.TestCase):
    TEST_FILE = 'tmp'

    def test_no_properties(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/no_properties', self.TEST_FILE)

        self.assertEqual(ErrorMessages.PROPERTIES, cm.exception.msg)

    def test_too_few_properties(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/too_few_properties', self.TEST_FILE)

        self.assertEqual(ErrorMessages.PROPERTIES, cm.exception.msg)

    def test_too_many_properties(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/too_many_properties', self.TEST_FILE)

        self.assertEqual(ErrorMessages.PROPERTIES, cm.exception.msg)

    def test_negative_properties(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/negative_properties', self.TEST_FILE)

        self.assertEqual(ErrorMessages.NEGATIVE_PROPERTIES, cm.exception.msg)

    def test_short_row(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/short_row', self.TEST_FILE)

        self.assertTrue(cm.exception.msg.startswith(ErrorMessages.SHORT_ROW[:20]))

    def test_unknown_symbol(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/unknown_symbol', self.TEST_FILE)

        self.assertTrue(cm.exception.msg.startswith(ErrorMessages.UNKNOWN_SYMBOL[:10]))

    def test_negative_weight(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/negative_weight', self.TEST_FILE)

        self.assertTrue(cm.exception.msg.startswith(ErrorMessages.UNKNOWN_SYMBOL[:10]))

    def test_too_big_weight(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/too_big_weight', self.TEST_FILE)

        self.assertTrue(cm.exception.msg.startswith(ErrorMessages.WEIGHT_BOUNDS[:10]))

    def test_low_corrected_weight(self):
        with self.assertRaises(ParseException) as cm:
            solve('invalid_inputs/low_corrected_weight', self.TEST_FILE)

        self.assertTrue(cm.exception.msg.startswith(ErrorMessages.LOW_CORRECTED_WEIGHT[:10]))

    def tearDown(self):
        if os.path.isfile(self.TEST_FILE):
            os.remove(self.TEST_FILE)
