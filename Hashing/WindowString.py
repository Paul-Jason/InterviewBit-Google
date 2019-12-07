class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def minWindow(self, A, B):
        largeStrLen = len(A)
        smallStrLen = len(B)
        #Forming small string Hash 
        smallStrHash = {}
        for l in range(0, smallStrLen):
            if B[l] in smallStrHash:
                smallStrHash[B[l]] = smallStrHash[B[l]] + 1
            else:
                smallStrHash[B[l]] = 1
        minWindowStr = ''
        #Finding the limits to get that window
        for i in range(0, largeStrLen):
            for j in range(i, largeStrLen):
                if((j-i) >= (smallStrLen-1)):
                    windowPresent = self.checkPresenceInWindow(A,i,j,smallStrHash)
                    if(windowPresent):
                        minWindowStrTemp = A[i:j+1]
                        if(minWindowStr == "" or len(minWindowStrTemp) < len(minWindowStr)):
                            minWindowStr = minWindowStrTemp
                            break
        return minWindowStr

    def checkPresenceInWindow(self,A,i,j,smallStrHash):
        largeStrHash = {}
        windowPresent = False
        #Forming the hash with count of characters from string A
        for k in range(i, j+1):
            if A[k] in largeStrHash:
                largeStrHash[A[k]] = largeStrHash[A[k]] + 1
            else:
                largeStrHash[A[k]] = 1
        largeStrHashLen = len(largeStrHash)
        smallStrHashLen = len(smallStrHash)
        #Not all charactes uniquely present in small string are not present in large String 
        if(largeStrHashLen >= smallStrHashLen):
            for smallStrHashKey in smallStrHash:
                if smallStrHashKey in largeStrHash:
                    if(largeStrHash[smallStrHashKey] != smallStrHash[smallStrHashKey]):
                        return windowPresent
                #Not everything is present
                else:
                    return windowPresent
            #If successfully came out of for which means all B chars are there in A window
            windowPresent = True
            return windowPresent
        else:
            return windowPresent

A = "ADOBECODEBANC"
B = "ABC"     
obj = Solution()   
obj.minWindow(A,B)
