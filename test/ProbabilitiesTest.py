import unittest
import Parser
import Probabilities


class ProbabilitiesTest(unittest.TestCase):
    def test_get_probs(self):
        game = Parser.parse_game('inputs/004')

        probs = Probabilities.get_raw_probs(game.groups)
        Probabilities.correct_probs(probs, game.groups)
        # TODO add tests for probability
