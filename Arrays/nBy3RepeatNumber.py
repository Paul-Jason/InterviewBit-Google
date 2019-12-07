class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        cacheDict = {}
        leng = len(A)
        for i in range(0,leng):
            ele = A[i]
            if(ele in cacheDict):
                cacheDict[ele] = cacheDict[ele] + 1
            else:
                cacheDict[ele] = 1
        thresold = leng // 3
        for key in cacheDict:
            if(cacheDict[key] > thresold):
                return key
        return -1

A = [1,2,3,1,1]
Solution().repeatedNumber(A)