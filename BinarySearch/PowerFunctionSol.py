#https://www.techiedelight.com/power-function-implementation-recursive-iterative/
#Check the above you may understand.

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        res = 1 % d  # Cover case d == 1
        while n > 0:
            if n & 1:   # Odd?
               res = (res * x) % d
            x = x**2 % d
            n >>= 1
        return res

x = 2
n = 3
d = 3

Solution().pow(x ,n ,d)