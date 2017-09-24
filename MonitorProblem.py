from problem import Problem
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
            i = 0
            for sensor in state:
                if sensor == 0: # or i == len(state)-1:
                    break
                elif sensor != 0:
                    i += 1

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
    def goal_test(self, state):
        #each target is being viewed by a sensor
        return False




    #state will be a tuple as large as the sensors array