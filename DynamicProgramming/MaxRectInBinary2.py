import numpy as np

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        arr = np.array(A, dtype = np.int)
        maxArea = 0
        rows = arr.shape[0]
        cols = arr.shape[1]
        for row in range(0, rows):
            for col in range(0, cols):
                startEle = arr[row][col]
                if(startEle == 1):
                    width = 1
                    height = 1
                    #Increase width and heigth in steps of 1
                    i = row 
                    j = col
                    moreWidthPoss = True
                    moreHeightPoss = True
                    while( i < rows - 1 or j < cols - 1):
                        if(moreWidthPoss and j < cols - 1):
                            j = j + 1
                            #Check all ones in that column until that height
                            for k in range(row, row + height):
                                if(arr[k][j] != 1):
                                    moreWidthPoss = False
                                    break
                            if(moreWidthPoss):
                                width = width + 1
                        if(j == cols - 1):
                            moreWidthPoss = False
                        if(moreHeightPoss and i < rows - 1):
                            i = i + 1
                            for k in range(col, col + width):
                                if(arr[i][k] != 1):
                                    moreHeightPoss = False
                                    break
                            if(moreHeightPoss):
                                height = height + 1
                        if(i == rows - 1):
                            moreHeightPoss = False
                        if( (not moreHeightPoss) and (not moreWidthPoss) ):
                            break
                    area = width * height
                    if(area > maxArea):
                        maxArea = area
        return maxArea
        
A = [
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]
Solution().maximalRectangle(A)