import util
import os
import csv
from search import *

class RoutePlanning:

    def __init__(self, start, goal):
        self.connectionsGraph:dict = dict()
        self.heuristicsGraph:dict = dict()
        self.start = start
        self.current = self.start
        self.goal = goal
        self.cities:list = list()
        
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace("Code", "CSV")
        os.chdir(dir)
        notFirst = False
        with open("cities.csv") as file:
            for line in file:
                line = line.strip()
                self.cities.append(line)
                self.connectionsGraph[line] = []
                self.heuristicsGraph[line] = []
        with open("Connections.csv") as file:
            for line in file:
                line = line.strip().split(",")
                if notFirst:
                    for i in range(len(self.cities)):
                        self.connectionsGraph[line[0]].append(int(line[i + 1]))
                notFirst = True
        notFirst = False
        with open("heuristics.csv") as file:
            for line in file:
                line = line.strip().split(",")
                if notFirst:
                    for i in range(len(self.cities)):
                        self.heuristicsGraph[line[0]].append(int(line[i + 1]))
                notFirst = True


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

        return state == self.goal    
    
    def _stateIndex(self, state):
        return self.cities.index(state)
    
    def _indexState(self, index):
        return self.cities[index]

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        successors = []
        for i in range(len(self.connectionsGraph[state])):
            # checking for a possible direct path
            if self.connectionsGraph[state][i] not in [-1, 0]: 
                successor = self._indexState(i)
                successors.append((successor, "Move", self.connectionsGraph[state][i]))
        return successors

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        # at the 0 index we have the current and at the 1 index we have the successor
        successor = self._stateIndex(actions[1])
        return self.connectionsGraph[actions[0]][successor]
                       
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        successor = self._stateIndex(state)
        return self.heuristicsGraph[self.goal][successor]
    
# route = RoutePlanning("Muzaffarabad", "Khunjerab Pass")
# route = RoutePlanning("Islamabad", "Hunza")
route = RoutePlanning("Kaghan", "Gilgit")

print(aStarSearch(route))
