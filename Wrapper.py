from MonitorProblem import MonitorProblem
from UniCost import UniCost
from BreadthFirst import BreadthFirst
from IDDFS import IDDFS
class Wrapper:
    def main(self):
        #Take in config file
        config_path = input("What is the path to the config file?\n")
        config_file = open(config_path, "r")
        config = config_file.read().splitlines()
        
        problem = None
        if(config[0] == 'monitor'):
            problem = MonitorProblem(config[1], config[2])
        else:
            print("Not a supported type of problem.")

        search_type = input("What type of search would you like to perform?")
        if(search_type == 'bfs'):
            print(BreadthFirst().breadth_first_tree_search(problem).state)
        elif search_type == 'unicost':
            print(UniCost().uniform_cost_search(problem).state)
        elif search_type == 'iddfs':
            print(IDDFS().Iterative_Deepening_Search(problem).state)

if __name__ == '__main__':
   Wrapper().main()
