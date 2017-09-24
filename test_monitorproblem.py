import unittest
import unittest.mock
from unittest.mock import MagicMock
from MonitorProblem import MonitorProblem

class TestMonitorProblemClass(unittest.TestCase):
    def test_init(self):
        mon_prob = None
        assert mon_prob == None
        mon_prob = MonitorProblem([("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)], [("T_1",1,2), ("T_2",3,3), ("T_3",0,5)])
        assert mon_prob != None
    
    def test_actions_return_size(self):
        #expect length of 3 because there are 3 targets
        mon_prob = MonitorProblem([("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)], [("T_1",1,2), ("T_2",3,3), ("T_3",0,5)])
        actions = mon_prob.actions([1, 0, 0, 0])
        #print(actions)
        assert len(actions) == 3

        #expected to return an array with no length if given a full state
        mon_prob2 = MonitorProblem([1, 2, 3], ['a', 'b', 'c'])
        actions2 = mon_prob2.actions([1, 1, 2])
        assert len(actions2) == 0

        #if there are zero targets then an empty array should be returned
        mon_prob3 = MonitorProblem([1, 2, 3], [])
        actions3 = mon_prob3.actions([1, 0, 0])
        assert len(actions3) == 0

    def test_actions_return_contents(self):
        #expect length of 3 because there are 3 targets
        mon_prob = MonitorProblem([("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)], [("T_1",1,2), ("T_2",3,3), ("T_3",0,5)])
        actions = mon_prob.actions([1, 0, 0, 0])
        #print(actions)
        assert actions == [[1, 1, 0, 0], [1, 2, 0, 0], [1, 3, 0, 0]]
        actions = mon_prob.actions(actions[2])
        assert actions == [[1, 3, 1, 0], [1, 3, 2, 0], [1, 3, 3, 0]]
        actions = mon_prob.actions(actions[1])
        assert actions == [[1, 3, 2, 1], [1, 3, 2, 2], [1, 3, 2, 3]]

        #expected to return an array with no length if given a full state
        mon_prob2 = MonitorProblem([1, 2, 3], ['a', 'b', 'c'])
        actions2 = mon_prob2.actions([1, 1, 2])
        assert actions2 == []

        #if there are zero targets then an empty array should be returned
        mon_prob3 = MonitorProblem([1, 2, 3], [])
        actions3 = mon_prob3.actions([1, 0, 0])
        assert actions3 == []
