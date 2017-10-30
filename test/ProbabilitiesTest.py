import unittest
import Parser
import Probabilities


class ProbabilitiesTest(unittest.TestCase):
    def test_get_probs(self):
        field, m, n, _ = Parser.parse_field('inputs/input1')
        groups = Parser.get_groups(field, m, n)

        probs = Probabilities.get_probs(groups)
        Probabilities.print_probs(probs, field, m, n)

