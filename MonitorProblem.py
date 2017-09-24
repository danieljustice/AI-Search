from problem import Problem
import math
class MonitorProblem(Problem):
    def __init__(self, sensors, targets):
        self.sensors = sensors
        self.targets = targets
        self.initial_state = [0 for sensor in self.sensors]

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
        return action
    
    def goal_test(self, state):
        #each target is being viewed by a sensor
        is_goal = True
        num_targets = len(self.targets)
        for i in range(1, num_targets + 1):
            if i not in state:
                is_goal = False
        return is_goal

    def path_cost(self, state):
        path_cost_list = []
        sensor_index = 0
        for sensor in state:
            if sensor != 0:
                individual_cost = self.time_monitored(self.sensors[sensor_index], self.targets[sensor-1])
                path_cost_list.append(individual_cost)
            else:
                path_cost_list.append(0)
        sensor_index += 1

        for i, this_sensor in enumerate(state):
            for j, other_sensor in enumerate(state):
                if i != j:
                    if this_sensor == other_sensor:
                        if path_cost_list[i] < path_cost_list[j]:
                            path_cost_list[i] = 0
                        else:
                            path_cost_list[j] = 0

        
        return sum(path_cost_list)



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
        print(sensor)
        print(target)
        x = sensor[1] - target[1]
        print(x)
        y = sensor[2] - target[2]
        distance = math.sqrt(x**2 + y**2)
        print(distance)
        #time is power divided by distance
        time = sensor[3]/distance
        print(time)
        return time
