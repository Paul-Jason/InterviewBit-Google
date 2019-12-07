import numpy as np

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        arr = np.array(A, dtype = np.int)
        maxArea = 0
        for row in arr:
            for cell in row:
                ele = arr[row][cell]
                if(ele == 1):
                    width = 1
                    height = 1
                    #See left from here
                    for l in range(cell - 1 ,-1, -1):
                        if(arr[row][l] == 1):
                            width = width + 1
                        else:
                            break
                    #See right from here
                    for r in range(cell + 1 , arr.shape[1]):
                        if(arr[row][r] == 1):
                            width = width + 1
                        else:
                            break
                    #See top from here
                    for t in range(row - 1, -1, -1):
                        if(arr[t][cell] == 1):
                            height = height + 1
                        else:
                            break
                    #See bottom from here
                    for b in range(row + 1, arr.shape[0]):
                        if(arr[b][cell] == 1):
                            height = height + 1
                        else:
                            break
                area = width * height
                if(area > maxArea):
                    maxArea = area
        return maxArea
A = [
    [1,1,1],
    [0,1,1],
    [1,0,0]
]
Solution().maximalRectangle(A)