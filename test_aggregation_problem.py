import unittest
import unittest.mock
from unittest.mock import MagicMock
from AggregationProblem import AggregationProblem

class TestAggregationProblemClass(unittest.TestCase):
    def test_actions(self):
        ap = AggregationProblem('[("N_1",1,1), ("N_2",2,3), ("N_3",1,5)]', 
                                ['("N_1","N_3",4)', '("N_1","N_2",10)', '("N_2","N_3",5)'])
        action_list = ap.actions(ap.initial)
        print(action_list)
        print(ap.initial)
        
        action_list = ap.actions(["N_2"])
        print(action_list)
        assert ap.actions(ap.initial)[0] == ('N_1', 'N_3', 4)
