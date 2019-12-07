# Did it in O(k^2) space complexity need to do it in O(k) space not time
import numpy as np 

k = int(input())
k = k + 1
#k is 0 based
arr = np.zeros([2,k],dtype=int)
arr[0][0] = 1
for nthrow in range(1,k):
    for i in range(0,nthrow+1):
        if(i == 0):
            arr[1][i] = 1
        elif(i == nthrow):
            arr[1][i] = 1
        else:
            arr[1][i] = arr[0][i-1] + arr[0][i]
    arr[0] = arr[1]
print(arr[1])