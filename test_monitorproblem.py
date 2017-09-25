import unittest
import unittest.mock
from unittest.mock import MagicMock
from MonitorProblem import MonitorProblem

class TestMonitorProblemClass(unittest.TestCase):
    def test_init(self):
        mon_prob = None
        assert mon_prob == None
        mon_prob = MonitorProblem('[("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)]', '[("T_1",1,2), ("T_2",3,3), ("T_3",0,5)]')
        assert mon_prob != None
    
    def test_actions_return_size(self):
        #expect length of 3 because there are 3 targets
        mon_prob = MonitorProblem('[("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)]', '[("T_1",1,2), ("T_2",3,3), ("T_3",0,5)]')
        actions = mon_prob.actions([1, 0, 0, 0])
        #print(actions)
        assert len(actions) == 3

        #expected to return an array with no length if given a full state
        mon_prob2 = MonitorProblem("[1, 2, 3]", "['a', 'b', 'c']")
        actions2 = mon_prob2.actions([1, 1, 2])
        assert len(actions2) == 0

        #if there are zero targets then an empty array should be returned
        mon_prob3 = MonitorProblem("[1, 2, 3]", "[]")
        actions3 = mon_prob3.actions([1, 0, 0])
        assert len(actions3) == 0

    def test_actions_return_contents(self):
        #expect length of 3 because there are 3 targets
        mon_prob = MonitorProblem('[("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)]', '[("T_1",1,2), ("T_2",3,3), ("T_3",0,5)]')
        actions = mon_prob.actions([1, 0, 0, 0])
        #print(actions)
        assert actions == [[1, 1, 0, 0], [1, 2, 0, 0], [1, 3, 0, 0]]
        actions = mon_prob.actions(actions[2])
        assert actions == [[1, 3, 1, 0], [1, 3, 2, 0], [1, 3, 3, 0]]
        actions = mon_prob.actions(actions[1])
        assert actions == [[1, 3, 2, 1], [1, 3, 2, 2], [1, 3, 2, 3]]

        #expected to return an array with no length if given a full state
        mon_prob2 = MonitorProblem("[1, 2, 3]", "['a', 'b', 'c']")
        actions2 = mon_prob2.actions([1, 1, 2])
        assert actions2 == []

        #if there are zero targets then an empty array should be returned
        mon_prob3 = MonitorProblem("[1, 2, 3]", "[]")
        actions3 = mon_prob3.actions([1, 0, 0])
        assert actions3 == []

    def test_is_goal(self):
        mon_prob = MonitorProblem("['x', 'y', 'z']", "['a', 'b', 'c']")
        assert mon_prob.goal_test([1, 2, 3]) == True
        assert mon_prob.goal_test([1, 2, 0]) == False
        assert mon_prob.goal_test([0, 2, 3]) == False
        #if there is a phantom sensor added, lets just count it
        assert mon_prob.goal_test([1, 2, 0, 3]) == True
        assert mon_prob.goal_test([3, 1, 2]) == True


        mon_prob3 = MonitorProblem("[1, 2, 3]", "[]")
        assert mon_prob3.goal_test([]) == True
        #assigning sensors to targets that dont exist? thats ok
        assert mon_prob3.goal_test([1, 2, 3]) == True
        
    def test_path_cost(self):
        mon_prob = MonitorProblem('[("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)]', '[("T_1",1,2), ("T_2",3,3), ("T_3",0,5)]')
       
        assert mon_prob.path_cost([1, 0, 0, 0]) == -100

    def test_time_monitored(self):
        mon_prob = MonitorProblem('[("S_1",1,1,100), ("S_2",2,3,88), ("S_3",1,5,120), ("S_4",1,4,240)]', '[("T_1",1,2), ("T_2",3,3), ("T_3",0,5)]')
        time = mon_prob.time_monitored(("S_2",2,3,88),("T_2",3,3))
        assert time == 88
