# No Data structure used pure logic.

import random

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        # Create a set with all the values in it
        vals = set()
        for elem in A:
            vals.add(elem)
        # Pick a value and keep searching on both sides of array
        # Repeat process until all elements in set are removed
        maxLen = 1
        while len(vals) > 0:
            val = random.sample(vals, 1)[0] # we know the length is greater than 0
            left = val-1
            right = val+1
            curLen = 1
            vals.remove(val) # remove this element since already visited
  
            while left in vals:
                curLen += 1
                vals.remove(left) # remove from the set to avoid visiting again
                left -=1 
            while right in vals:
                curLen += 1
                vals.remove(right)
                right += 1
            maxLen = max(curLen, maxLen)
        return maxLen

A = [100, 4, 200, 1, 3, 2]
Solution().longestConsecutive(A)
