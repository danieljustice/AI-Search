from MonitorProblem import MonitorProblem
from AggregationProblem import AggregationProblem
from UniCost import UniCost
from BreadthFirst import BreadthFirst
from Greedy import Greedy
from Astar import Astar
from IDDFS import IDDFS
from ast import literal_eval as make_tuple
from PancakesProblem import PancakesProblem
#argecho.py
import sys

class Wrapper:
    def main(self):
        config_path = sys.argv[1]
        search_type = sys.argv[2]
        #Take in config file
        # config_path = input("What is the path to the config file?\n")
        config_file = open(config_path, "r")
        config = config_file.read().splitlines()
        
        # search_type = input("What type of search would you like to perform?")


        problem = None
        if config[0].lower() == 'monitor':
            problem = MonitorProblem(config[1], config[2])
            answer = self.search(search_type, problem)
            if(answer is None):
                print("No answer for this search.")
            else:
                index = 0
                for sensor in answer.state:
                    print("S_", index+1, "_T_", answer.state[index])
                    index += 1
                print("Time: ", problem.time)
                print("Space: Frontier ", problem.frontier, " , Visited", problem.visited)
                print("Cost (Maximum Monitoring Time) ", -answer.path_cost)
                #print(answer.state, ",  ", -answer.path_cost)
        elif config[0].lower() == 'aggregation':
            cities = config[1]
            cities_list = make_tuple(cities)
            roads = config[2:]
            best_answer = None
            best_problem = None
            for city in cities_list:
                initial_state = city[0]
                problem = AggregationProblem(cities, roads, initial_state)
                answer = self.search(search_type, problem)
                if(answer is not None):
                    if(best_answer is None):
                        best_answer = answer
                        best_problem = problem
                    if(answer.path_cost < best_answer.path_cost):
                        #print(answer.state)
                        best_answer = answer
                        best_problem = problem
            if(answer is None):
                print("None for this search.")
            else:
                #print(answer.state, ",  ", answer.path_cost)
                for city in best_answer.state:
                    print(city)
                #print(answer.state)
                print("Time: ", best_problem.time)
                print("Space: Frontier ", best_problem.frontier, " , Visited", problem.visited)
                print("Cost (Maximum Monitoring Time) ", best_answer.path_cost)
        elif config[0].lower() == "pancakes":
            initial = config[1]
            goal = config[2]
            problem = PancakesProblem(initial, goal)
            answer = self.search(search_type, problem)
            if(answer is None):
                print("None for this search.")
            else:
                #print(answer.state, ",  ", answer.path_cost)
                index = 0
                #for sensor in answer.state:
                #    print("S_", index+1, "_T_", answer.state[index])
                #    index += 1
                print(answer.state)
                print("Time: ", problem.time)
                print("Space: Frontier ", problem.frontier, " , Visited", problem.visited)
                print("Cost (Maximum Monitoring Time) ", answer.path_cost)
        else:
            print(config[0], "is Not a supported type of problem.")







    def search(self, search_type, problem):
        if(search_type == 'bfs'):
            return BreadthFirst().breadth_first_tree_search(problem)    #node
        elif search_type == 'unicost':
            return UniCost().uniform_cost_search(problem)               #node
        elif search_type == 'iddfs':
            return IDDFS().Iterative_Deepening_Search(problem)          #node
        elif search_type == 'greedy':
            return Greedy().greedy_cost_search(problem)
        elif search_type == 'astar':
            return Astar().astar_cost_search(problem)

if __name__ == '__main__':
   Wrapper().main()


