from Node import Node
from Stack import Stack
class IDDFS:
    def depth_first_tree_search(self, problem):
        stack = Stack()
        node = Node(problem.initial)
        stack.push(node)

        while stack:
            node = stack.pop()
            print("pop: ", node.state)
            print("")
            if(problem.goal_test(node.state)):
                return node

            frontier_nodes = node.expand_frontier(problem)
            for fnode in frontier_nodes:
                print("push: ", fnode.state)
                stack.push(fnode)
        
        return None

    #ok, rethink this, IDDFS is basically redoing limited-depth search with new limits
#so lets make a limited-depth search
    '''
    Book sudo code for depth-limited    
    function D EPTH -L IMITED -S EARCH ( problem, limit ) returns a solution, or failure/cutoff
    return R ECURSIVE -DLS(M AKE -N ODE (problem.I NITIAL -S TATE ), problem, limit )
    function R ECURSIVE -DLS(node, problem, limit ) returns a solution, or failure/cutoff
    if problem.G OAL -T EST (node.S TATE ) then return S OLUTION (node)
    else if limit = 0 then return cutoff
    else
    cutoff occurred ? ← false
    for each action in problem.A CTIONS (node.S TATE ) do
    child ← C HILD -N ODE ( problem, node, action)
    result ← R ECURSIVE -DLS(child , problem, limit − 1)
    if result = cutoff then cutoff occurred ? ← true
    else if result  = failure then return result
    if cutoff occurred ? then return cutoff else return failure
    '''
    def depth_limited_search(self, problem, limit):
        return self.recursive_DLS(Node(problem.initial), problem, limit)

    def recursive_DLS(self, node, problem, limit=1):
        problem.time += 1
        if(problem.frontier < node.depth):
            problem.frontier = node.depth
        if(problem.goal_test(node.state)):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for action in problem.actions(node.state):
                child = node.child_node(problem, action)
                problem.visited += 1
                result = self.recursive_DLS(child, problem, limit-1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result != None:
                    return result
            if cutoff_occurred:
                return 'cutoff'
            else:
                return None


    '''
    Book pseudo code
    function I TERATIVE -D EEPENING -S EARCH ( problem) returns a solution, or failure
    for depth = 0 to ∞ do
    result ← D EPTH -L IMITED -S EARCH ( problem, depth)
    if result  = cutoff then return result
    '''

    def Iterative_Deepening_Search(self, problem):
        depth = 0
        while True:
            result = self.depth_limited_search(problem, depth)
            depth += 1
            if result != 'cutoff':
                return result