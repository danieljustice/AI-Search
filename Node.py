from problem import Problem
class Node:
    """Generalized Node class to work with any class inheriting the Problem.py."""
    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def child_node(self, problem, action):
        """create a child node from this node based off of the
        problem and current action"""
        #print("In child_node: ", action)
        next_node = problem.resulting_state(self.state, action)
        #print("next_node: ", next_node)
        if next_node is None:
            return None
        return Node(next_node, self, action,
                    problem.path_cost(self.path_cost, self.state, action, next_node))

    def expand_frontier(self, problem):
        """Returns all of the child nodes from this node"""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def node_path(self):
        """Returns a list of all of the nodes that led to this node"""
        node = self
        path = []
        while node:
            path.append(node)
            node = node.parent
        return list(reversed(path))

    def action_path(self):
        """Returns all of the actions that lead to this node"""
        #skip the first node because it can be assumed that no action
        #led to the first node
        return [node.action for node in self.node_path()[1:]]
