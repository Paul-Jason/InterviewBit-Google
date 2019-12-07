def binarySearch(A, B, startIndex, endIndex):
    mid = int((endIndex + startIndex) / 2)
    if(A[mid] <= B):
        if( A[mid + 1] >= B)            
            result = [mid+1, mid+2]
            return result
        else:
            binarySearch(A, B, mid+1, endIndex)

    else:
        if(A[mid - 1] <= B):
            result = [mid, mid + 1]
            return result
        else:
            binarySearch(A, B, startIndex, mid - 1)

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        leng = len(A)
        if(leng == 0 or leng == 1) : 
            return ([-1, 1])
        else:
            result = binarySearch(A, B, 0, leng-1)
            return result

A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10

Solution().searchRange(A,B)