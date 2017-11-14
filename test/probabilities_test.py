import unittest

from src import probabilities
from src import config as conf
from src.parser import parse_game


class ProbabilitiesTest(unittest.TestCase):
    # считаем, что отклонение не должно быть более 10% от точного значения
    DEVIATION = 0.1

    def test_raw_probs(self):
        a_set = {(0, 0), (0, 1), (0, 2)}
        b_set = {(1, 0), (1, 2), (2, 0), (2, 2)}
        c_set = {(3, 0), (3, 1), (3, 2)}

        game = parse_game('inputs/001')
        probs = probabilities.get_raw_probs(game.groups)

        for cell in a_set:
            self.assertTrue(abs(probs[cell] - 4. / 7) < conf.EPS)

        for cell in b_set:
            self.assertTrue(abs(probs[cell] - (1 - (1 - 4. / 7) * (1 - 3. / 7))) < conf.EPS)

        for cell in c_set:
            self.assertTrue(abs(probs[cell] - 3. / 7) < conf.EPS)

    def test_get_probs(self):
        game = parse_game('inputs/001')

        probs = probabilities.get_probs(game.groups)

        a_set = {(0, 0), (0, 1), (0, 2)}
        b_set = {(1, 0), (1, 2), (2, 0), (2, 2)}
        c_set = {(3, 0), (3, 1), (3, 2)}

        self.assertTrue(abs(sum(probs[cell] for cell in a_set | b_set) - 4) < conf.EPS)
        self.assertTrue(abs(sum(probs[cell] for cell in b_set | c_set) - 3) < conf.EPS)

        for cell in a_set:
            self.assertTrue(abs(probs[cell] - 52. / 78) < ProbabilitiesTest.DEVIATION)

        for cell in b_set:
            self.assertTrue(abs(probs[cell] - 39. / 78) < ProbabilitiesTest.DEVIATION)

        for cell in c_set:
            self.assertTrue(abs(probs[cell] - 28. / 78) < ProbabilitiesTest.DEVIATION)

