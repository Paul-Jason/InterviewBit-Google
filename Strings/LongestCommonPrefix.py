class Solution:
	# @param A : list of strings
	# @return a strings
    def longestCommonPrefix(self, A):
            leng = len(A)
            if(leng == 1):
                return A[0]
            else:
                #Form a initial prefix string
                firstStr = A[0]
                secondStr = A[1]
                minLeng = min(len(firstStr), len(secondStr))
                commonPrefix = ""
                for i in range(0, minLeng):
                    if(firstStr[i] == secondStr[i]):
                        commonPrefix = commonPrefix + firstStr[i]
                    else:
                        break
                if(len(commonPrefix) == 0):
                    return ""
                #After forming the initial one then compare it with every other string
                for i in range(2, leng):
                    #Take a string
                    presentStr = A[i]
                    newCommonPrefix = ""
                    minLeng = min(len(commonPrefix), len(presentStr))
                    for j in range(0, minLeng):
                        if(commonPrefix[j] == presentStr[j]):
                            newCommonPrefix = newCommonPrefix + presentStr[j]
                        else: 
                            #If new common prefix is ""
                            if(len(newCommonPrefix) == 0):
                                return ""
                    commonPrefix = newCommonPrefix
                print(commonPrefix)

A = ["abab", "ab", "abcd"]

Solution.longestCommonPrefix(Solution, A)