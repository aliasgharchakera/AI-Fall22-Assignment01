import util
from search import *

class JumpingFrogs():
    def __init__(self):
        self.current:list = "ggg0bbb"#["g","g","g","0","b","b","b"]
        self.start = self.current
        self.goal:list = "bbb0ggg"#["b","b","b","0","g","g","g"]
        
    
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        
        return self.start

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        return self.goal == state     

    def _switch(self, state, i, j):
        temp = ''
        return temp.join((state[:i], state[j], state[i+1:j], state[i], state[j+1:]))

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """   
        successors = []
        
        #index for empty rock
        rock = state.index('0')
        
        if rock-1 >=0 and state[rock-1] == "g":
            next_state = self._switch(state, rock-1, rock)
            successors.append((next_state, [state, next_state], 1))
        
        if rock-2 >=0 and state[rock-2] == "g":
            next_state = self._switch(state, rock-2, rock)
            successors.append((next_state, [state, next_state], 2))
        
        if rock+1 <=len(state)-1 and state[rock+1] == "b":
            next_state = self._switch(state, rock, rock+1)
            successors.append((next_state, [state, next_state], 1))
        
        if rock+2 <=len(state)-1 and state[rock+2] == "b":
            next_state = self._switch(state, rock, rock+2)
            successors.append((next_state, [state, next_state], 2))
        
        return successors


    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        return abs(actions[0].index("0") - actions[1].index("0")) # determining whether the jump is single or double    

        
    def getHeuristic(self, state):
        """
        state: the current state of agent

        THis function returns the heuristic of current state of the agent which will be the 
        estimated distance from goal.
        """
        heuristic = 0
        for i in range(len(state)):
            if state[i] != "b" and i < 3:
                for j in range(i, len(state)):
                    if state[j] == "b":
                        heuristic += j
            
            if state[i] != "g" and i > 3:
                for j in range(i):
                    if state[j] == "g":
                        heuristic += (i-j)
        return heuristic
    
frogs = JumpingFrogs()
print(aStarSearch(frogs))