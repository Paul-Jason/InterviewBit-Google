class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        leng = len(A)
        listOfList =[]
        listOfList.append(A.copy())
        for _ in range(1,leng):
            #Rotate array by 1
            last = A[leng-1]
            for j in range(leng-2, -1, -1):
                A[j+1] = A[j]
            A[0] = last
            listOfList.append(A.copy())
        return listOfList

A = [1,1,2]
Solution().permute(A)