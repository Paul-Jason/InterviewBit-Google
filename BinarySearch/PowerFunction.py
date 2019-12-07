class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if(n == 0 or x == 0):
            return pow(x,n) % d
        if( n % 2 == 1):
            multiRes = x
            return multiRes % d
        else:
            multiRes = x * x
            return multiRes % d

x = 2
n = 3
d = 3

Solution().pow(x ,n ,d)