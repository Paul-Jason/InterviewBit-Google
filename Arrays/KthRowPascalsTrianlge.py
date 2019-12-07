import numpy as np 

k = int(input())
k = k + 1
#k is 0 based
arr = np.zeros([k,k],dtype=int)
for i in range(0,k):
    for j in range(0,i+1):
        if(j == 0):
            arr[i][0] = 1
        elif(i == j):
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
print(arr[k-1])