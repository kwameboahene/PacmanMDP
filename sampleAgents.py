# sampleAgents.py
# parsons/07-oct-2017

# Version 1.1

# Some simple agents to work with the PacMan AI projects from:

# http://ai.berkeley.edu/

# These use a simple API that allow us to control Pacman's interaction with
# the environment adding a layer on top of the AI Berkeley code.

# As required by the licensing agreement for the PacMan AI we have:

# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# The agents here are extensions written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game




# class MDPAgent(Agent):

#     def __init__(self):

#         self.visited = []
#         self.capsules=[]
#         self.maxX = 0
#         self.maxY = 0
#         self.foodlist = []
#         self.wall = []
#         self.discount = 0.7
#         self.rewardfood = 10
#         self.rewardcapsule = 20
#         self.rewardaghost = -30
#         self.rewardghost = -50
#         self.rewardwall = 0
#         self.rewardmap = {}
#         self.states = 0
#         self.rewardnofood = 0
#         self.aroundghost = []
#         self.utilitiesmap = {}
#         self.iter = 150
#         self.converge = False
#         self.send = False
        

 

#     def final(self, state):

#         self.visited = []
#         self.capsules=[]
#         self.maxX = 0
#         self.maxY = 0
#         self.foodlist = []
#         self.capsules = []
#         self.wall = []
#         self.discount = 0.7
#         self.rewardfood = 10
#         self.rewardwall = 0
#         self.rewardnofood = 0
#         self.rewardaghost = -30
#         self.rewardghost = -50
#         self.rewardmap = {}
#         self.states = 0
#         self.aroundghost = []
#         self.utilitiesmap = {}
#         self.converge = False
#         self.send = False






# # this function takes all location with food and creates a map which
# # allocates a value of 10 to all location with food
#     def initializeMap(self,state):

#         legal = api.legalActions(state)
#         food = api.food(state)
#         walls = api.walls(state)
#         pacman = api.whereAmI(state)
#         ghosts = api.ghosts(state)
#         capsules = api.capsules(state)
#         corners = api.corners(state)
        
        
#         #add pacman location to visited locations 
#         if pacman not in self.visited:
#             self.visited.append(pacman)


#         #if states == 0 this means a new game has began
#         #there we create a reward map and assign 
#         if self.states == 0:

        

            
#             #coordinates with no food and capsules and aren't walls
#             NoFoodCoord=[]

#             for i in range(0,len(corners)):

#                 if corners[i][0] > self.maxX:
#                     self.maxX = corners[i][0] 
#                 if corners[i][1] > self.maxY:
#                     self.maxY = corners[i][1] 



#             for x in range(0,self.maxX+1):
#                 for y in range(0,self.maxY+1):

#                     #add coordinate to wall and set utility for wall to 0
#                     if(x, y) in walls:
#                         self.wall.append((x, y))


#                     #add coordinate to food list
#                     if(x, y) in food:
#                         self.foodlist.append((x, y))

#                     #add coordinate to capsule list
#                     if (x, y) in capsules:
#                         self.capsules.append((x, y))

#                     #add coordinate that have no food and capsule and walls
#                     if (x, y) not in walls and (x, y) not in food and (x, y) not in capsules:
#                         NoFoodCoord.append((x, y))


        
#             foodsdict  = dict.fromkeys(self.foodlist,self.rewardfood)
#             capsuledict = dict.fromkeys(self.capsules,self.rewardcapsule)
#             nofooddict = dict.fromkeys(NoFoodCoord,self.rewardnofood)
#             walldict = dict.fromkeys(self.wall,self.rewardwall)

#             #create reward map
#             rewardmap = {}
            
#             rewardmap.update(foodsdict)
#             rewardmap.update(capsuledict)
#             rewardmap.update(nofooddict)
#             rewardmap.update(walldict)

#             for ghost in ghosts:
#                 self.aroundghost = self.aroundGhost(ghost)

#             for i in self.aroundghost:
#                 rewardmap[i] = self.rewardaghost

#             for ghost in ghosts:
#                 rewardmap[(int(ghost[0]), int(ghost[1]))] = self.rewardghost



#             self.rewardmap = rewardmap



#             self.utilitiesmap = rewardmap

#             #print self.utilitiesmap

            
#             self.states += 1

#             print "state is " + str(self.states)




#         #if number of game states >= 1
#         else:

#             if pacman in self.foodlist:
#                 self.foodlist.remove(pacman)
#                 print "pacman removed"

#             if pacman in self.capsules:
#                 self.capsules.remove(pacman)

#             self.rewardmap[pacman] = self.rewardnofood

#             self.states += 1

#             for (x, y) in self.rewardmap:

#                 if(x, y) in walls:
#                     self.rewardmap[(x, y)] = self.rewardwall


#                 if(x, y) in food:
#                     self.rewardmap[(x, y)] = self.rewardfood

#                 #add coordinate to capsule list
#                 if (x, y) in capsules:
#                     self.rewardmap[(x, y)] = self.rewardcapsule

#                 #add coordinate that have no food and capsule and walls
#                 if (x, y) not in walls and (x, y) not in food and (x, y) not in capsules:
#                     self.rewardmap[(x, y)] = self.rewardnofood


#             ghosts = api.ghostStates(state)


#             for ghost in ghosts:

#                 if ghost[1] == 1 and (int(ghost[0][0]), int(ghost[0][1])) in self.foodlist:

#                     self.rewardmap[(int(ghost[0][0]), int(ghost[0][1]))] = self.rewardghost

#                 if ghost[1] == 1 and (int(ghost[0][0]), int(ghost[0][1])) not in self.foodlist:

#                     self.rewardmap[(int(ghost[0][0]), int(ghost[0][1]))] = self.rewardghost


#             ghosts = api.ghostStatesWithTimes(state)


#             for  ghost in ghosts:

#                 if ghost[1] >= 6 and (int(ghost[0][0]), int(ghost[0][1])) in self.foodlist:

#                     self.rewardmap[(int(ghost[0][0]), int(ghost[0][1]))] = self.rewardfood

#                     self.aroundghost = self.aroundGhost(ghost[0])

#                     for i in self.aroundghost:

#                         if i in self.foodlist:
#                             self.rewardmap[i] = self.rewardfood

#                         else:
#                             self.rewardmap[i] = self.rewardnofood

#                 elif ghost[1] >= 6 and (int(ghost[0][0]), int(ghost[0][1])) not in self.foodlist:

#                     self.rewardmap[(int(ghost[0][0]), int(ghost[0][1]))] = self.rewardnofood

#                     self.aroundghost = self.aroundGhost(ghost[0])

#                     for i in self.aroundghost:

#                         if i in self.foodlist:
#                             self.rewardmap[i] = self.rewardfood

#                         else:
#                             self.rewardmap[i] = self.rewardnofood

#                 else:

#                     self.rewardmap[(int(ghost[0][0]), int(ghost[0][1]))] = self.rewardghost

#                     self.aroundghost = self.aroundGhost(ghost[0])

#                     for i in self.aroundghost:

    
#                         self.rewardmap[i] = self.rewardaghost








            


            
            
#             #print  "State is " + str(self.states)



        





        
#     # this function calculates the maximum expected utility for a location
#     #in the Map 
#     # the formula for meu = (value of intended direction * 0.8) + (0.1 * value of left direction) +
#     # + (0.1 * value of right direction)
#     def maxEU(self, walls, loc):


#         self.x = loc[0]
#         self.y = loc[1]

#         #print walls

#         current = (self.x, self.y)
#         east = (self.x+1, self.y)
#         west = (self.x-1, self.y)
#         south =(self.x, self.y-1)
#         north = (self.x, self.y+1)


        

#         utility = {"north_util": 0.0, "east_util": 0.0, "south_util": 0.0, "west_util": 0.0}

#         west_util = 0
#         east_util= 0
#         south_util = 0
#         north_util = 0



        
#         # if inteded direction is west of current location
#         if  west not in walls: 

#             west_util += (0.8 *  self.utilitiesmap[west])

#         else:
#             west_util += (0.8 *  self.utilitiesmap[current])


#         if   north not in walls:

#             west_util += (0.1 * self.utilitiesmap[north])

#         else:
#             west_util += (0.1 * self.utilitiesmap[current])


#         if   south not in walls:

#             west_util += (0.1 * self.utilitiesmap[south])

#         else:
#             west_util += (0.1 * self.utilitiesmap[current])
        

#         utility["west_util"] = west_util


#         # if intended direction is east of current location
#         if  east not in walls:

#             east_util += (0.8 * self.utilitiesmap[east])

#         else:
#             east_util += (0.8 * self.utilitiesmap[current])

#         if  north not in walls:

#             east_util += (0.1 * self.utilitiesmap[north])

#         else:
#             east_util += (0.1 * self.utilitiesmap[current])

#         if  south not in walls:

#             east_util += (0.1 * self.utilitiesmap[south])

#         else:
#             east_util += (0.1 * self.utilitiesmap[current])

        
#         utility["east_util"] = east_util


#         # if intended direction is south of current location
#         if   south not in walls:

#             south_util = (0.8 * self.utilitiesmap[south])

#         else:
#             south_util = (0.8 * self.utilitiesmap[current])

#         if   east not in walls:

#             south_util += (0.1 * self.utilitiesmap[east])

#         else:
#             south_util += (0.1 * self.utilitiesmap[current])

#         if   west not in walls:

#             south_util += (0.1 * self.utilitiesmap[west])

#         else:
#             south_util += (0.1 * self.utilitiesmap[current])


#         utility["south_util"] = south_util


#         ## if intended direction is north of current location
#         if   north not in walls:

#             north_util += (0.8 * self.utilitiesmap[north])

#         else:
#             north_util += (0.8 * self.utilitiesmap[current])


#         if  east not in walls:

#             north_util += (0.1 * self.utilitiesmap[east])

#         else:
#             north_util += (0.1 * self.utilitiesmap[current])      


#         if   west not in walls:

#             north_util += (0.1 * self.utilitiesmap[west])

#         else:
#             north_util += (0.1 * self.utilitiesmap[current])
        

#         utility["north_util"] = north_util



#         if self.send == False:

#             print utility

#             return utility[max(utility, key=utility.get)]

#         else:
#             return utility

        
        





#     def valueIteration(self,state,gamma):
#         # This function is an implementation of value iteration 
#         # it takes as inputs, the discount gamma
#         # the reward value
#         #and utilities of the coordinates
     

#         legal = api.legalActions(state)


#         if Directions.STOP in legal:
#             legal.remove(Directions.STOP)


#         self.converge = False

#         while self.converge == False:

#             convergencevalue = 0.0
                     
#             newutilities = self.utilitiesmap.copy()

#             for x in range(1,self.maxX):

#                 for y in range(1,self.maxY):

#                     if  (x, y) not in self.wall :
 
#                         newutilities[(x, y)] = self.rewardmap[(x, y)] + gamma * self.maxEU(self.wall, (x, y))
                        
            
#                         convergencevalue += abs(newutilities[(x, y)] - self.utilitiesmap[(x, y)])
            
#             #print convergencevalue

#             self.utilitiesmap = newutilities

#             if convergencevalue < 0.1:

#                 self.converge = True
#                 break

#             #iterations +=1








#     def aroundGhost(self,ghosts):
#         #this function returns cordinates 4 steps 
#         # to the north, west, south and east of ghosts
#         coord = []

#         #print ghosts

#         #east of ghost
#         if ( int(ghosts[0]) +1 , int(ghosts[1])) not in coord:
#                 if (int(ghosts[0])+ 1 , int(ghosts[1])) not in self.wall:
#                     coord.append((int(ghosts[0])+ 1 , int(ghosts[1])))
#         #west of ghost
#         if (int(ghosts[0])- 1 , int(ghosts[1])) not in coord:
#                 if (int(ghosts[0])- 1, int(ghosts[1])) not in self.wall:
#                     coord.append((int(ghosts[0])- 1, int(ghosts[1])))
#         #south of ghost
#         if (int(ghosts[0]), int(ghosts[1])-1) not in coord:
#             if (int(ghosts[0]) , int(ghosts[1])-1) not in self.wall:
#                 coord.append((int(ghosts[0]) , int(ghosts[1]-1)) )
        
#         #north of ghost
#         if (int(ghosts[0]) , int(ghosts[1])+1) not in coord:
#             if (int(ghosts[0]) , int(ghosts[1])+1) not in self.wall:
#                 coord.append( (int(ghosts[0]) , int(ghosts[1]+1)) )

#         #northeast of ghost
#         if ( int(ghosts[0]) +1 , int(ghosts[1])+1) not in coord:
#                 if ( int(ghosts[0]) +1 , int(ghosts[1])+1) not in self.wall:
#                     coord.append(( int(ghosts[0]) +1 , int(ghosts[1])+1))
#         #northwest of ghost
#         if (int(ghosts[0])- 1 , int(ghosts[1]) + 1) not in coord:
#                 if (int(ghosts[0])- 1 , int(ghosts[1]) + 1) not in self.wall:
#                     coord.append((int(ghosts[0])- 1 , int(ghosts[1]) + 1))
#         #southeast of ghost
#         if (int(ghosts[0]) + 1, int(ghosts[1])-1) not in coord:
#             if (int(ghosts[0]) + 1, int(ghosts[1])-1) not in self.wall:
#                 coord.append((int(ghosts[0]) + 1, int(ghosts[1])-1) )
        
#         #southwest of ghost
#         if (int(ghosts[0]) -1, int(ghosts[1])-1) not in coord:
#             if (int(ghosts[0]) -1, int(ghosts[1])-1) not in self.wall:
#                 coord.append( (int(ghosts[0]) -1, int(ghosts[1])-1) )

#         return coord




#     def PacmanEU(self,pacman,legal):



#         self.returnutility = True

#         utility = self.maxEU(self.wall, pacman)

#         self.returnutility = False

#         #print self.utilitiesmap


#         maxeu = -100000000
#         direct = None

#         if Directions.STOP in legal:
#             legal.remove(Directions.STOP)

#         for direction in legal:

#             if direction == Directions.NORTH:

#                 if utility["north_util"] > maxeu:
#                     maxeu = utility["north_util"] 
#                     direct = "north_util"


#             if direction == Directions.SOUTH:

#                 if utility["south_util"] > maxeu:
#                     maxeu = utility["south_util"] 
#                     direct = "south_util"


#             if direction == Directions.EAST:

#                 if utility["east_util"] > maxeu:
#                     maxeu = utility["east_util"] 
#                     direct = "east_util"


#             if direction == Directions.WEST:

#                 if utility["west_util"] > maxeu:
#                     maxeu = utility["west_util"] 
#                     direct = "west_util"

        
#         #print maxeu
#         #print utility
#         print direct

#         return direct





#     def getAction(self,state):

#         #get location of pacman
#         pacman = api.whereAmI(state) 

#         #print pacman

#         self.initializeMap(state)


#         self.valueIteration(state,self.discount)


#         legal = api.legalActions(state)

#         if Directions.STOP in legal:
#             legal.remove(Directions.STOP)


#         direction = self.PacmanEU(pacman,legal)

#         if  direction == "north_util":
#             #print "north_util"
#             return api.makeMove(Directions.NORTH, legal)

#         elif direction == "south_util":
#             #print "south_util"
#             return api.makeMove(Directions.SOUTH, legal)

#         elif direction == "east_util":
#             #print "east_util"
#             return api.makeMove(Directions.EAST, legal)

#         else: 
#             #print "west_util"
#             return api.makeMove(Directions.WEST, legal)




