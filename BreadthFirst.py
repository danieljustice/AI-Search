from Queue import Queue
from Node import Node
class BreadthFirst:
    def breadth_first_tree_search(self, problem):
        queue = Queue()
        node = Node(problem.initial, None, None, 0)
        queue.enqueue(node)

        while queue:
            node = queue.dequeue()
            if(problem.goal_test(node.state)):
                return node
           
            frontier_nodes = node.expand_frontier(problem)
            for fnode in frontier_nodes:
                queue.enqueue(fnode)

        return None
