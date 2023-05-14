from FourRooms import FourRooms

import numpy as np
import sys
import random
import time


# initialise all values of the q-table to zero
QTable = np.zeros((13, 13, 4))
RTable =  np.zeros((13, 13, 4))

def epsilon_greedy_policy(Qtable, state, epsilon, pos):
        action = random.uniform(0,1)
        if action > epsilon:
            action = maxAction(pos, False)

            while(valid(pos, action)==False):
                action = maxAction(pos, False)
            
        else:
            action = random.randint(0, 3) # select a random action

            while(valid(pos, action)==False):
                action = np.random.randint(0,4)

        return action

# method to check the validity of the current position of the agent 
def valid(pos,action):
    if(RTable[pos][action]==-1):
        return False
    return True

# get the maximum action you can take from the Q table
def maxAction(pos, new_pos):
    state_actions = [QTable[pos][0],QTable[pos][1],QTable[pos][2],QTable[pos][3]]
    q = max(state_actions) # get the max action from the states possible actions
    
    # if this is a new position we want to find the maximum value for the next action
    if(new_pos==True):
        return q
    
    # use the current pos to find the max action if the all the q-values are the same chose random action
    ran = np.random.choice([i for i in range(len(state_actions)) if state_actions[i] == q])
    return ran

def setUp():
    for i in range (13):
            for j in range(13):
                if(i == 0 or i == 12 or j == 0 or j == 12 or i == 6):
                    for k in range(4):
                       RTable[(i,j)][k] = -1
    h = [(6,3),(6,10)]
    for i in h:
        RTable[i][0] = -1
        RTable[i][1] = -1
        RTable[i][2] = 0
        RTable[i][3] = 0
    h2 = [(2,6),(9,7)]
    for i in h2:
        RTable[i][0] = 0
        RTable[i][1] = 0
        RTable[i][2] = -1
        RTable[i][3] = -1
    neg = [(1,6),(3,6),(4,6),(5,6),(7,7),(8,7),(10,7),(11,7)]
    for i in neg:
        for a in range(4):
            RTable[i][a] = -1

def main():

    stochastic = False

    # CLI
    if(len(sys.argv) >1):
        if(sys.argv[1] == '-stochastic'):
            stochastic = True

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple', stochastic)

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']
    
    # set up the r table
    setUp()
    
    # define variables to use for updating the q-value
    epsilon = 0.8
    learningrate = 0.6
    discountfactor = 0.5

    for epoch in range (20):
        # get the current position of the agent
        currentPos = fourRoomsObj.getPosition()
        # check if the isTerminal is reached to stop loop
        # isTerminal = fourRoomsObj.isTerminal()
        while True:
            # determine the next action
            currentAction = epsilon_greedy_policy(QTable, currentPos, epsilon, currentPos )

            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(currentAction)

            # check if the package was found by taking the action
            if gridType > 0:
                RTable[currentPos][currentAction] = 100

            print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[currentAction], newPos, gTypes[gridType]))


            reward = RTable[currentPos][currentAction]
            
            temporaldiff = reward + discountfactor * (np.max(QTable[newPos])-QTable[currentPos][currentAction])
            # q table being updated with the formula
            QTable[currentPos][currentAction] = QTable[currentPos][currentAction] + learningrate *  (temporaldiff)

            currentPos = newPos

            if fourRoomsObj.isTerminal():
                break

        print ("Done with epoch")
        print(epoch)
        fourRoomsObj.showPath(-1,"image.png")
        fourRoomsObj.newEpoch()
        # decay of epsilon to allow the agent to exploit the environment more
        if(epsilon>0):
            epsilon-=0.05
            
if __name__ == "__main__":
    main()
