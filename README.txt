Python Version 3.5.2+

Libraries: ast, math, unnittest, unnitest.mock

resources:  https://github.com/aimacode
            https://stackoverflow.com/
            https://docs.python.org/3/c-api/index.html
            Artificial Intelligence: A Modern Approach (3rd Edition)

Credits:    Kat Hetzel - Healthy debate on node generation. Should it
                         be generated on the fly or at the beginning?

            Rebecca Addison - Problem formulation as discussed in the book



How to run: 
        1)in terminal 'python3 puzzlesolver.py'
        2)when asked for file path, type file. 
        3)when asked for search type, enter one of: 
                                    [bfs, iddfs, uncost]
                                    NOTE: no spaces
        4) Output will be either a tuple being (state, cost)
            or it will state "None for this search."



Example: 
        terminal:   python3 puzzlesolver.py
        prompt:     What is the path to the config file?
        user:       monitor.config
        prompt:     What type of search would you like to perform?
        user:       unicost
        prompt:     [1, 1, 3, 2] ,   -100.0


Known Problems:
            1) Input arguments should be taken in when program is started
                        currently they are passed in while running
            2) Greedy and A* not Supported