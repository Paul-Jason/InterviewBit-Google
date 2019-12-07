import numpy as np 

#Factorial stored used dynamic programming
factDP = []
# fact(0)
factDP.append(1)

def computeFactorial(n):
    if(n >= 0):
        leng = len(factDP)
        if(n > leng - 1):
            for i in range(leng, n+1):
                factDP.append( i * factDP[i-1] )
        return factDP[n]

class Solution:

    def uniquePaths(A, B):
        # Formula is (m+n-2)! / (n-1)! * (m-1)!
        x = computeFactorial( A + B - 2)
        y = computeFactorial( A -1 )
        z = computeFactorial( B - 1 )
        result = int(x / y * z)
        print(result)
        
computeFactorial(5)