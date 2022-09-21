import util
import os
import csv
from search import *

class RoutePlanning:

    def __init__(self, start, goal):
        self.graph = {}
        self.start = start
        self.current = self.start
        self.goal = goal
        
        files = ["cities.csv", "Connections.csv", "heuristics.csv"]
        path = os.path.realpath(__file__) # Gives the path of demo.py    
        dir = os.path.dirname(path) # Gives the directory where this .py exists
        dir = dir.replace("Code", "CSV")
        os.chdir(dir)

        for f in files:
            with open(f) as file:
                reader = csv.reader(file)
                count = 0
                for row in reader:
                    if f == 'cities.csv':
                        self.graph[row[0]] = {} # Add all the cities as keys in the dictionary
                    elif f == 'Connections.csv':
                        if count == 0:
                            cities = row[1:] # Adding all the cities except for the first since it is same as key
                        else:
                            for i in range(len(row[1:])): # Ignore index 1 as it is the city name that is the key and not the weights/ distances
                                self.graph[row[0]][cities[i]] = [int(row[i+1])] # {source1: {destination1: [distance], ...}, ...}
                                # Row 0 is the respective city
                    elif f == 'heuristics.csv':
                        if count == 0:
                            cities = row[1:]
                        else:
                            for i in range(len(cities)):
                                self.graph[row[0]][cities[i]].append(int(row[i+1])) # {source1: {destination1: [distance, heuristic], ...}, ...}
                    count += 1


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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        successors = []
        for key in self.graph[state]:
            # checking for a possible direct path
            if self.graph[state][key][0] != 0 and self.graph[state][key][0] != -1: 
                successors.append((key, "Move", self.graph[state][key][0]))
        return successors

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        # at the 0 index we have the current and at the 1 index we have the successor
        return self.graph[actions[0]][actions[1]][0]
                       
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        return self.graph[self.goal][state][1]
    
route = RoutePlanning("Muzaffarabad", "Khunjerab Pass")
print(aStarSearch(route))
