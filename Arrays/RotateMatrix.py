import numpy as np 

arr = [
    [1,2],
    [3,4]
]
n = len(arr)
rotatedArray = np.empty((n,n), dtype= int)
# First row will become last column in rotated array and so on.
for i in range(0, n):
    for j in range(0, n):
        rotatedArray[j][n - i - 1] = arr[i][j]
print(rotatedArray) 