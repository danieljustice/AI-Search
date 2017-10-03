from problem import Problem
import math
from ast import literal_eval as make_tuple
from Queue import Queue
'''
This is basically the traveling salesman problem, so im gonna
name variables as such
'''


class AggregationProblem(Problem):
    def __init__(self, cities, roads, initial = None):
        self.time = 0
        self.visited = 0
        self.frontier = 0
        self.cities = make_tuple(cities)
        #print("length: ", len(self.cities), "cities: ", self.cities)
        self.roads =  [make_tuple(road.replace("\n", "")) for road in roads if road != " "]                  #self.split_into_tuples(roads)
        #print(self.roads)
        if initial == None:
            #print(self.cities[1])
            self.initial = [self.cities[0][0]]
        else:
            self.initial = [initial]
        #print(self.initial)

    def actions(self, state):
        #print("Begin actions")
        #print(state)
        action_list = []
        for road in self.roads:
            if(state[len(state)-1] == road[0]):
                action_list.append(road)
            if(state[len(state)-1] == road[1]):
                reverse_road = (road[1], road[0], road[2])
                action_list.append(reverse_road)
        #print(action_list)
        #print("End actions")
        return action_list


    #push next node onto the states queue
    def resulting_state(self, state, action):
        new_state = state[:]
        if(action[1] not in state):
            new_state.append(action[1])
        #print("state: " ,  state, " action: ", action)
        #print("old state: ", state, " new state: ", new_state)
        return new_state



    def path_cost(self, state1_cost, state1, action, state2=None):
        new_cost = state1_cost + action[2] 
        return new_cost

    
    def goal_test(self, state):
        #if(state is not None):
         #   print("len(state): ", len(state), " len(cities): ", len(self.cities))
        #else:
         #   print("None")
        return len(state) == len(self.cities)



    def split_into_tuples(self, string):

        temp_str = string.replace("[", "")
        temp_str = temp_str.replace("]", "")
        if temp_str == "":
            return []
        tuple_string_list = temp_str.split(", ")
        tuple_list = []
        for sensor in tuple_string_list:
            tuple_list.append(make_tuple(sensor))
        return tuple_list
    
    def value(self, state):
        """give increased value to states where 
        current city is closer to all the other un-visited cities"""
        sum_of_distances = 0
        for city in self.cities:
            if city[0] not in state:
                for current_city in self.cities:
                    if current_city[0] == state[len(state)-1]:
                        sum_of_distances += self.find_distance(current_city, city)
    
        return sum_of_distances

    def find_distance(self, city1, city2):
        x = city1[1] - city2[1]
        y = city1[2] - city2[2]
        return math.sqrt(x**2 + y**2)