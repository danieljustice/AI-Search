from problem import Problem
import math
from ast import literal_eval as make_tuple


class PancakesProblem(Problem):
    def __init__(self, initial, goal = None):
        #take in as a string, make into tuple, cast to list
        self.time = 0
        self.visited = 0
        self.frontier = 0
        self.initial = list(make_tuple(initial))
        if goal == None:
            self.goal = []
            i = 1
            for item in self.initial:
                self.goal.append(i)
                i+=1
        else:
            self.goal = list(make_tuple(goal))

    def actions(self, state):
        action_list = []
        index = 0
        for item in state:
            action_list.append(self.flip(state, index))
            index+=1
        return action_list

    def resulting_state(self, state, action):
        return action

    def path_cost(self, state1_cost, state1, action, state2=None):
        #new_cost = state1_cost + 1
        num_same = 0
        index = 0
        for item in state1:
            if item == action[index]:
                num_same +=1
            index += 1
        new_cost = num_same/len(state1)
        #print(new_cost)
        return -new_cost

    def goal_test(self, state):
        return self.goal == state

    def flip(self, array, index):
        first_half = array[:index+1]
        second_half = array[index+1:]
        r_first_half = first_half[::-1]
        n_r_first_half = [x*-1 for x in r_first_half]
        #print(first_half, "        ", n_r_first_half)
        return n_r_first_half + second_half

    def value(self, state):
        """give increased value to states with more pancakes in 
        the correct place"""
        num_correct = 0
        index = 1
        for pancake in state:
            if pancake == index:
                num_correct+=1
        
        return -num_correct



