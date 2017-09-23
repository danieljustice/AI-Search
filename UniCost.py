from PriorityQueue import PriorityQueue

class UniCost:

    def uniform_cost_search(self, problem):
        #lambda function to compare in the priority queue
        f = lambda node: node.path_cost
        
        #make node from initial node
        #node = Node(problem.initial)

        #create pq for frontier
        pw = PriorityQueue(min, f)

        #push to pq

        #check if it is goal state


        #if not goal state check get new nodes and push to priority

