class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        leng = len(A)
        for i in range(0, leng):
            if(i < (leng-1) ):
                if(A[i] == A[i+1] or A[i] > A[i+1]):
                    for j in range(i+1, leng):
                        if( (A[i+1] < A[j])):
                            if(A[j] > A[i]):
                                A[i+1] = A[j]
                                break
            #Completed check
            if(A[i] == A[leng -1]):
                if( (i+1) < leng):
                    for k in range(len(A) - 1 , i, -1): 
                        A.pop(k)
                    break
                
        newLeng = len(A)
        return newLeng

A = [ 0, 0, 0, 1, 1, 2, 2, 3 ]
Solution.removeDuplicates(Solution,A)
