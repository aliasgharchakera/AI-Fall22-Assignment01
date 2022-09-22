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

from tracemalloc import start
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





def aStarSearch(problem: SearchProblem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR A* CODE HERE ***"

    start = problem.getStartState()
    priorityQueue = util.PriorityQueue()
    priorityQueue.push(start, 0)

    cost_dict = {start: None}
    total = {start: 0}

    path = []

    while not priorityQueue.isEmpty():
        problem.current = priorityQueue.pop()

        if problem.isGoalState(problem.current):
            break

        for successor in problem.getSuccessors(problem.current):
            successor = successor[0] # since it is a triplet
            updated_cost = total[problem.current] + problem.getCostOfActions([problem.current, successor])

            if successor not in total.keys() or updated_cost < total[successor]:
                total[successor] = updated_cost 
                priority = updated_cost + problem.getHeuristic(successor)
                cost_dict[successor] = problem.current
                priorityQueue.update(successor, priority)

        if not problem.isGoalState(problem.current):
            goal = problem.goal
            while goal in cost_dict.keys():
                path.append(goal)
                goal = cost_dict[goal]

    path = path[::-1]
    path = path[:path.index(problem.goal)+1]

    return path, total[problem.goal]

 

# cities = "CSV/cities.csv"
# Connections = "CSV/Connections.csv"
# heuristics = "CSV/heuristics.csv"
# x = RoutePlanning("Naran", "Murree")
# print(x.getSuccessors("Islamabad"))
