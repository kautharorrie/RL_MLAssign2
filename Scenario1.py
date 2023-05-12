from FourRooms import FourRooms

import numpy as np
import sys
import random


def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    # initialise all values of the q-table to zero
    QTable = np.zeros((13, 13, 4))
    # QTable[11,0,3] = 50
    # QTable[11,5,2] = 100

    # In the epsilon_greedy_policy we will:

    # 1. Generate the random number between 0 to 1.
    # 2. If the random number is greater than epsilon, we will do exploitation. It means that the agent will take the action with the highest value given a state.
    # 3 . Else, we will do exploration (Taking random action). 

    def epsilon_greedy_policy(Qtable, state, epsilon):
        random_int = random.uniform(0,1)
        if random_int > epsilon:
            # print("PLOITING")
            action = np.argmax(Qtable[state])
        else:
            action = random.randint(0, 3) # select a random action
            # print("EXP")
        return action

    # define a reward function
    rewardFunction = np.array(
         
            [
                # 0   1   2   3   4   5   6   7   8   9  10  11  12
                [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100],  # 0
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 1
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  1,  -1,  -1,  -1,  -1, -100],  # 2
                [-100,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1, -100],  # 3
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 4
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 5
                [-100, -100,  -1, -100, -100, -100, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 6
                [-100,  -1,  -1,  -1,  -1,  -1, -100, -100, -100,  -1, -100, -100, -100],  # 7
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 8
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 9
                [-100,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1, -100],  # 10
                [-100,  -1,  -1,  -1,  -1,  -1, -100,  -1,  -1,  -1,  -1,  -1, -100],  # 11
                [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100]   # 12
            ], dtype=np.float32
        )


    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))

    

    # define the variables
    state = fourRoomsObj.getPosition()
    learning_rate = 0.1
    discountfactor = 0.5

    # Exploration parameters
    max_epsilon = 1.0           
    min_epsilon = 0.05           
    decay_rate = 0.0005 


    for episode in range(100):


        epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode)
        while True:
            reward = rewardFunction[state] 
            isTerminal = False
            gridType = 0
            newPos = (0, 0)
            packagesRemaining = 0

            r = epsilon_greedy_policy(QTable, state, epsilon)
            # r = random.randint(0, 3)
            if r == 0:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            elif r == 1:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            elif r == 2:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            elif r == 3:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            # q table being updated with the formula
            QTable[state] = QTable[state] + learning_rate * (reward + discountfactor * (np.max(QTable[newPos])-QTable[state]) )
            if isTerminal:
                # print(episode)
                break
        fourRoomsObj.showPath(-1, savefig= "image.png")
        fourRoomsObj.newEpoch()

    # Don't forget to call newEpoch when you start a new simulation run
    for episode in range(10):
        fourRoomsObj.newEpoch()
        state = fourRoomsObj.getPosition()
        isTerminal = False
        while True:
            action = np.argmax(QTable(state))
            # isTerminal = False
            if action == 0:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            elif action == 1:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            elif action == 2:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            elif action == 3:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
                # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
                state = newPos

            if isTerminal:
                break

        fourRoomsObj.showPath(-1, savefig= "final.png")

    # Show Path
    # fourRoomsObj.showPath(-1, savefig= "image.png")
    # h = (11, 5)
    # print(np.max(q_values[h]))

    print(QTable)

if __name__ == "__main__":
    main()
