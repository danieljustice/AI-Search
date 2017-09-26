from MonitorProblem import MonitorProblem
from AggregationProblem import AggregationProblem
from UniCost import UniCost
from BreadthFirst import BreadthFirst
from IDDFS import IDDFS
from ast import literal_eval as make_tuple
class Wrapper:
    def main(self):
        #Take in config file
        config_path = input("What is the path to the config file?\n")
        config_file = open(config_path, "r")
        config = config_file.read().splitlines()
        
        search_type = input("What type of search would you like to perform?")


        problem = None
        if config[0] == 'monitor':
            problem = MonitorProblem(config[1], config[2])
            self.search(search_type, problem)
        elif config[0] == 'aggregation':
            cities = config[1]
            cities_list = make_tuple(cities)
            roads = config[2:]

            for city in cities_list:
                initial_state = city[0]
                problem = AggregationProblem(cities, roads, initial_state)
                answer = self.search(search_type, problem)
                if(answer is None):
                    print("None for this search.")
                else:
                    print(answer.state, ",  ", answer.path_cost)

        else:
            print("Not a supported type of problem.")







    def search(self, search_type, problem):
        if(search_type == 'bfs'):
            return BreadthFirst().breadth_first_tree_search(problem)    #node
        elif search_type == 'unicost':
            return UniCost().uniform_cost_search(problem)               #node
        elif search_type == 'iddfs':
            return IDDFS().Iterative_Deepening_Search(problem)          #node



if __name__ == '__main__':
   Wrapper().main()


