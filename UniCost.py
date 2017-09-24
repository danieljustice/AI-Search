from PriorityQueue import PriorityQueue
from Node import Node
class UniCost:

    def uniform_cost_search(self, problem):
        #lambda function to compare in the priority queue
        f = lambda node: node.path_cost

        #make node from initial node
        node = Node(problem.initial)

        #create pq for frontier
        pq = PriorityQueue(min, f)

        #push to pq
        pq.enqueue(node)

        #set of explored states
        #use set because contains is quicker in sets than lists
        #set of states, not nodes because we dont want duplicate states, nodes dont matter
        explored = set()

        #loop until pq is empty ---- or goal state is reached?
        while pq:
            node = pq.dequeue()
            #check if it is goal state
            if problem.goal_test(node.state):
                #if goal state return node
                return node
            #otherwise, build out new nodes and push to pq
            else:
                explored.add(node.state)
                #array of child nodes
                frontier_nodes = node.expand_frontier()
                #push them onto pq
                for fnode in frontier_nodes:
                    #dont want duplicates, so can't exist in explored or pq
                    if fnode.state not in explored and fnode not in pq:
                        pq.enqueue(fnode)
                    #if by chance there is a duplicate node in frontier,
                    #delete the "larger"/worst node
                    elif fnode in pq:
                        current_node = pq[fnode]
                        if f(fnode) < f(current_node):
                            del pq[current_node]
                            pq.enqueue(fnode)
        #if a node was not returned at this point, nothing matches the goal state
        return None
