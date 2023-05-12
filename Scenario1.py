from FourRooms import FourRooms

import numpy as np
import sys
import random


def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    q_values = np.zeros((13, 13, 4))
    q_values[11,0,3] = 50
    q_values[11,5,2] = 100

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

    for episodes in range(1000):

        r = random.randint(0, 3)
        if r == 0:
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
            print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))

        elif r == 1:
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
            print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))

        elif r == 2:
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
            print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
        
        elif r == 3:
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
            print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))
        
        
        # gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.action)

        # print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[r], newPos, gTypes[gridType]))

        # print(action)

        if isTerminal:
            print(episodes)
            break

        # fourRoomsObj.newEpoch()

    # Don't forget to call newEpoch when you start a new simulation run

    # Show Path
    fourRoomsObj.showPath(-1, savefig= "image.png")
    h = (11, 5)
    print(np.max(q_values[h]))

if __name__ == "__main__":
    main()
