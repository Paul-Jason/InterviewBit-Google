def nearestLower(arr):
    ''' return indices of nearest lower element '''
    res = []
    for i, x in enumerate(arr):
        j = i-1
        while j>=0 and arr[j]>=x:
            j = res[j]
        res.append(j)
    return res

def biggestRectangle(hist):
    
    n = len(hist)
    best = 0
    for x, i, j in zip(hist,
        nearestLower(hist),
    	reversed(nearestLower(list(reversed(hist))))):
        best = max(best, x*(n-1-j-(i+1)))
    return best

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
	    ''' Run lenght accumulation by column:
	        we compute height of contiguous sequence of 1.
	        Then it boils to find biggest rectange in histogram.
	    '''
	    if not A:
	        return 0
	    n = len(A[0])
	    hist = [0] * n
	    best = 0
	    for row in A:
	        for i, x in enumerate(row):
	            if x:
	                hist[i] += 1
	            else:
	                hist[i] = 0
	        best = max(best, biggestRectangle(hist))
	    return best

A = [  
        [1, 1, 1],
        [0, 1, 1],
        [1, 0, 0] 
    ]
Solution().maximalRectangle(A)