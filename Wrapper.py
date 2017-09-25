from MonitorProblem import MonitorProblem
from UniCost import UniCost
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

        print(UniCost().uniform_cost_search(problem).state)


if __name__ == '__main__':
   Wrapper().main()
