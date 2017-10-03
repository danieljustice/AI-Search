from PriorityQueue import PriorityQueue
from Node import Node
class Astar:

    def astar_cost_search(self, problem):
        #lambda function to compare in the priority queue
        f = lambda node: problem.value(node.state) + node.path_cost

        #make node from initial node
        node = Node(problem.initial,None, None, 0, 0)

        #create pq for frontier
        pq = PriorityQueue(min, f)

        #push to pq
        pq.enqueue(node)

        #set of explored states
        #use set because contains is quicker in sets than lists
        #set of states, not nodes because we dont want duplicate states, nodes dont matter
        explored = []

        #loop until pq is empty ---- or goal state is reached?
        while pq.size() > 0:
            node = pq.dequeue()
            #print("woot", node.state, " costs ", node.path_cost)
            #check if it is goal state
            if problem.goal_test(node.state):
                #if goal state return node
                return node
            #otherwise, build out new nodes and push to pq
            else:
                explored.append(node.state)
                problem.visited += 1
                #array of child nodes
                frontier_nodes = node.expand_frontier(problem)
                #frontier_states = [(x.state, x.path_cost) for x in frontier_nodes]
                #print("frontier: ", frontier_states)
                #push them onto pq
                for fnode in frontier_nodes:
                    #dont want duplicates, so can't exist in explored or pq
                    if fnode.state not in explored and fnode not in pq:
                        pq.enqueue(fnode)
                        problem.time += 1
                        if(pq.size() > problem.frontier):
                            problem.frontier = pq.size()
                    #if by chance there is a duplicate node in frontier,
                    #delete the "larger"/worst node
                    elif fnode in pq:
                        #print(fnode.node_path())
                        #print(pq.size())
                        current_node = pq[fnode]
                        #print(current_node)
                        if f(fnode) < f(current_node):
                            del pq[current_node]
                            pq.enqueue(fnode)
        #if a node was not returned at this point, nothing matches the goal state
        return None
