# Possible unique paths from start to finish.
# Possible movements - RIGHT or DOWN

import numpy as np 

def checkMoreRoutesPossible(grid):
    result = np.any(grid)
    return result

A = 2
B = 2
grid = np.ones((A,B), dtype= int)
grid[0][0] = 0
grid[A-1][B-1] = 0
noOfRoutesPossible = 0
moreRoutesPossible = True
thisRoutePossible = True
restart = True
previousStepDown = 0
while restart:
    for i in range(0, A):
        for j in range(previousStepDown, B):
            if(i == A - 1 and j == B - 1):
                noOfRoutesPossible = noOfRoutesPossible + 1
                moreRoutesPossible = checkMoreRoutesPossible(grid)
                if(moreRoutesPossible):
                    i = 0
                    j = 0
                else:
                    moreRoutesPossible = False
                    restart = False
            # First see if you can down then right because once you go right you may miss one route you cant go left after going down
            elif(i+1 < A):
                if(grid[i+1][j] == 1):
                    grid[i][j] = 0
                    previousStepDown = j
                    break
                else:
                    if(j < B):
                        if(grid[i][j] == 1):
                            grid[i][j] = 0
                        else:
                            thisRoutePossible = False
                            moreRoutesPossible = checkMoreRoutesPossible(grid)
                            if(moreRoutesPossible):
                                i = 0
                                j = 0
                            else:
                                moreRoutesPossible = False
                                restart = False
            #Step down is not possible then go for step right
            elif(j+1 < B):
                if(grid[i][j+1] == 1):
                    grid[i][j+1] = 0
                else:
                    thisRoutePossible = False
                    moreRoutesPossible = checkMoreRoutesPossible(grid)
                    if(moreRoutesPossible):
                        i = 0
                        j = 0
                    else:
                        moreRoutesPossible = False
                        restart = False
        if(not moreRoutesPossible):
            break
print(noOfRoutesPossible) 