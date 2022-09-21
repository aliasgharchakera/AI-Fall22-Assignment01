# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import heapq
import math

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        pass       
        # util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        pass       
        # util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        pass       
        # util.raiseNotDefined()
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        pass       
        # util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        pass       
        # util.raiseNotDefined()

class JumpingFrogs():
    def __init__(self):
        self.current_state:list = "GGG BBB"#["G","G","G"," ","B","B","B"]
        self.start_state = self.current_state
        self.goal:list = "BBB GGG"#["B","B","B", " ","G","G","G"]
        
    
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        
        return self.start_state
        # util.raiseNotDefined()

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        if self.goal == state:
            return True
        return False       

    def swap(self, state, i, j):
        str1 = ''
        
        return str1.join((state[:i], state[j], state[i+1:j], state[i], state[j+1:]))

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
        rock = state.index(' ')
        
        if rock-1 >=0 and state[rock-1] == "G":
            
            next_state = self.swap(state, rock-1, rock)
            successors.append((next_state, [state, next_state], 1))
        
        if rock-2 >=0 and state[rock-2] == "G":
            next_state = self.swap(state, rock-2, rock)
            successors.append((next_state, [state, next_state], 2))
        
        if rock+1 <=len(state)-1 and state[rock+1] == "B":
            next_state = self.swap(state, rock, rock+1)
            successors.append((next_state, [state, next_state], 1))
        
        if rock+2 <=len(state)-1 and state[rock+2] == "B":
            next_state = self.swap(state, rock, rock+2)
            successors.append((next_state, [state, next_state], 2))
        
        return successors


    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        pass       

        
    def getHeuristic(self,state):
        """
        state: the current state of agent

        THis function returns the heuristic of current state of the agent which will be the 
        estimated distance from goal.
        """
        heuristic = 0
        for i in range(len(state)):
            if state[i] != "B" and i < 3:
                for j in range(i, len(state)):
                    if state[j] == "B":
                        heuristic += j
            
            if state[i] != "G" and i > 3:
                for j in range(i):
                    if state[j] == "G":
                        heuristic += (i-j)
        return heuristic

class RoutePlanning:

    def __init__(self, cities, connection, heuristics, start, goal):
        self.cities:list = list()
        self.connect_dict:dict = dict()
        self.heuristic_dict:dict = dict()

        self.start = start
        self.goal = goal
        self.current:str = self.start

        with open(cities) as f:
            for city in f:
                self.cities.append(city.strip())

        with open(connection) as f:
            x = 0
            for line in f:
                if x != 0:
                    my_line = line.split(",")
                    self.connect_dict[my_line[0].strip()] = my_line[1:]
                    # print(self.connect_dict[my_line[0]])
                x = 1

        with open(heuristics) as f:
            x = 0
            for line in f:
                if x != 0:
                    my_line = line.split(",")
                    self.heuristic_dict[my_line[0].strip()] = my_line[1:]
                x = 1


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

        return True if self.current == self.goal else False       

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        connecs:list = list()
        
        temp:list = self.connect_dict[state]
        temp_tup:tuple = tuple()

        for i in range(len(temp)):
            if temp[i] != '-1' and temp[i]!= '0':
                temp_tup = (self.cities[i], 1, eval(temp[i]))
                connecs.append(temp_tup)

        return connecs

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        temp:str = str()
        nxt:str = str()
        cost:int = 0

        for i in range(len(actions) - 1):
            tmp = actions[i]
            nxt = actions[i+1]

            idx = self.cities.index(nxt)
            cost_list = self.connect_dict[temp]
            cost += int(cost_list[idx])

        return cost
                       
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        idx = self.heuristic_ref.index(self.goal)

        return int(self.heuristic_dict[state][idx])


def aStarSearch(problem: SearchProblem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR A* CODE HERE ***"

    open_q:util.PriorityQueue = util.PriorityQueue()
    closed_lst = list()
    cost:int = int()

    path_dict = dict()
    cost_dict = dict()

    open_q.push(problem.getStartState(), problem.getHeuristic(problem.getStartState()))
    path_dict[problem.getStartState()] = None #[state] = parent
    cost_dict[problem.getStartState()] = 0

    while(not open_q.isEmpty()):
        current = open_q.pop()
        closed_lst.append(current)

        if problem.isGoalState(current):
            break

        try:
            curr_nbrs = problem.getSuccessors(current) #0: name, 2:cost
        except:
            continue

        for nbr in curr_nbrs:
            nbr_name = nbr[0]
            
            if nbr_name not in path_dict.keys():
                path_dict[nbr_name] = current
            

            #func_g =  + problem.getHeuristic(nbr_name)
            cost = cost_dict[current] + nbr[2]

            if nbr_name not in cost_dict.keys() or cost < cost_dict[nbr_name]:  #update 
                cost_dict[nbr_name] = cost
                path_dict[nbr_name] = current
                open_q.push(nbr_name, cost + problem.getHeuristic(nbr_name) )

    return get_action_path(path_dict, problem.goal)


 


def get_action_path(path_dict:dict, state):

    current_state = state
    traversal = list()

    while current_state != None:
        traversal.append(current_state)
        current_state = path_dict[current_state]

    traversal.reverse()
    return traversal

cities = "CSV/cities.csv"
Connections = "CSV/Connections.csv"
heuristics = "CSV/heuristics.csv"
x = RoutePlanning(cities, Connections, heuristics, "Naran", "Murree")
print(x.getSuccessors("Islamabad"))

# x = JumpingFrogs()
# print(aStarSearch(x))