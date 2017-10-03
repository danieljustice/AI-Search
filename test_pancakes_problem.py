import unittest
import unittest.mock
from unittest.mock import MagicMock
from PancakesProblem import PancakesProblem

class TestPancakesProblem(unittest.TestCase):
    def test_flip(self):
        pan_prob = PancakesProblem('(-1,-11,-3,-6,-9,-4,-7,-10,-5,-8,-2)')
        flipped = pan_prob.flip([-1,-11,-3,-6,-9,-4,-7,-10,-5,-8,-2], 3)
        assert flipped == [6,3,11,1,-9,-4,-7,-10,-5,-8,-2]