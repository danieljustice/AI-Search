class Problem:
    """Abstract Class that describes the fucntionality of a search problem"""
    def __init__(self, initial_state, goal_func=None):
        """Constructor function that takes in the intial state of the problem
        and the function that describes a succesful goal. If no goal_func
        is given it will be assumed there is no goal function."""
        self.initial_state = initial_state
        self.goal_func = goal_func

    def actions(self, state):
        """Returns the possible actions that can be executed from the
        state passed in here."""
        raise NotImplementedError

    def resulting_state(self, state, action):
        """Returns the resulting state spawns from the state passed in
        and the action passed in to this function."""
        raise NotImplementedError
    
    def goal_test(self, state):
        """Runs the state throught the goal state lambda function,
        returns true if it is a goal state, false otherwise"""
        return self.goal_func(state)

    def path_cost(self, current_cost, state1, action, state2):
        """Currently just adds 1 to the current_cost. Only works for 
        uniform cost graphs. Expected override for non-uniform costs"""
        return current_cost + 1
