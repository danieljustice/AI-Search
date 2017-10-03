from problem import Problem
import math
from ast import literal_eval as make_tuple
class MonitorProblem(Problem):
    def __init__(self, sensors, targets):
        self.sensors = make_tuple(sensors)
        self.targets = make_tuple(targets)
        self.initial = [0 for sensor in self.sensors]
        self.time = 0
        self.visited = 0
        self.frontier = 0

    def actions(self, state):
        #if last sensor in state is not 0, then all sensors are assigned a target, no possible actions left
        if state[len(state)-1] != 0:
            return []
        else:
            #go to next sensor not assigned, spawn as many actions as there are targets
            i = self.find_unassigned_sensor(state)

            action_list = []
            j = 1
            for target in self.targets:
                temp_state = state[:]
                #print(temp_state)
                #print(i)
                #print(j)
                temp_state[i] = j
                #print(temp_state) #uncomment for debug
                action_list.append(temp_state)
                j += 1
            return action_list

    def resulting_state(self, state, action):
        #the result of going to the next state is the state
        #print(action," costs ", self.path_cost(action))

        return action
    
    def goal_test(self, state):
        #each target is being viewed by a sensor
        is_goal = True
        num_targets = len(self.targets)
        for i in range(1, num_targets + 1):
            if i not in state:
                is_goal = False
        return is_goal

    def path_cost(self, c, state, action = None, state2 = None):
        path_cost_list = []
        sensor_index = 0
        #print("state: ", state)
        for sensor in state2:
            if sensor != 0:
                individual_cost = self.time_monitored(self.sensors[sensor_index], self.targets[sensor-1])
                #print("sensor: ", self.sensors[sensor_index], " target: ", self.targets[sensor-1], " cost: ", individual_cost)
                path_cost_list.append(individual_cost)
            else:
                path_cost_list.append(0)
            sensor_index += 1

        for i, this_sensor in enumerate(state2):
            for j, other_sensor in enumerate(state2):
                if i != j:
                    if this_sensor == other_sensor:
                        if path_cost_list[i] < path_cost_list[j]:
                            path_cost_list[i] = path_cost_list[j]
                        else:
                            path_cost_list[j] = path_cost_list[i]
        #print ("state: ", state, "   path cost: ",  path_cost_list)
        path_cost_list[:] = [x for x in path_cost_list if x != 0]
        #print ("state: ", state, "   path cost: ",  path_cost_list)
        #print (path_cost_list, " min: ", min(path_cost_list))
        #print(state, "costs ", path_cost_list, " sum: ", sum(path_cost_list))
        return -min(path_cost_list)



    def find_unassigned_sensor(self, state):
        #go to next sensor not assigned, spawn as many actions as there are targets
        i = 0
        for sensor in state:
            if sensor == 0: # or i == len(state)-1:
                break
            elif sensor != 0:
                i += 1
        return i

    def time_monitored(self, sensor, target):
        #get euclidean distance
        #print(sensor)
        #print(target)
        #print(sensor, " ", target[1])
        x = sensor[1] - target[1]
        #print(x)
        y = sensor[2] - target[2]
        distance = math.sqrt(x**2 + y**2)
        #print(distance)
        #time is power divided by distance
        time = sensor[3]/distance
        #print(time)
        return time

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
        """give increased value to states where sensors are closer to targets"""
        sum_of_closest = 0
        index = 1
        for target in self.targets:
            if(index not in state):
                sum_of_closest += self.find_closest_sensor(target)[0]
        return sum_of_closest

    def find_closest_sensor(self, target):
        distances = []
        for sensor in self.sensors:
            x = sensor[1] - target[1]
            y = sensor[2] - target[2]
            distances.append(math.sqrt(x**2 + y**2))
        min_d = min(distances)
        return (min_d, distances.index(min_d))
