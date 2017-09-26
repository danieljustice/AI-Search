from Queue import Queue
from Node import Node
class BreadthFirst:
    def breadth_first_tree_search(self, problem):
        queue = Queue()
        node = Node(problem.initial, None, None, 0)
        queue.enqueue(node)
        #print("problem initial = ",  problem.initial)
        while not queue.is_empty():
            node = queue.dequeue()
            #print(node.state)
            if(problem.goal_test(node.state)):
                #print("goal reached: ", node.state)
                return node
           
            frontier_nodes = node.expand_frontier(problem)
            #print("frontier: ", frontier_nodes.state)
            for fnode in frontier_nodes:
                #print(fnode)
                if(fnode != None):
                    queue.enqueue(fnode)

        return None



