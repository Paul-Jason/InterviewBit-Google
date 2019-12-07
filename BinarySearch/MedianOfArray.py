def findMedian(A):
    l = len(A)
    mid = int(l/2)
    if(l % 2 == 0):
        # Length is even
        median = (float(A[mid-1]) + A[mid]) / 2
        return median
    else:
        median = float(A[mid]) 
        return median
        
A = [ -37, -9, 10, 19 ]
B = [ -29, 18, 46 ]

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays( A, B):
            m = len(A)
            n = len(B)
            totalLeng = m + n
            mid = int(totalLeng / 2)
            mergedArray = []
            arr1Pointer = 0
            arr2Pointer = 0
            # Forming the merged array that is good enough for finding the median
            if(m == 0  or n == 0):
                if(m == 0):
                    return findMedian(B)
                else:
                    return findMedian(A)
            for i in range(0, mid + 1):
                if(arr1Pointer > m-1):
                    mergedArray.append(B[arr2Pointer])
                    arr2Pointer = arr2Pointer + 1
                    continue
                elif (arr2Pointer > n-1):
                    mergedArray.append(A[arr1Pointer])
                    arr1Pointer = arr1Pointer + 1
                    continue
                if(A[arr1Pointer] <= B[arr2Pointer]):
                    mergedArray.append(A[arr1Pointer])
                    arr1Pointer = arr1Pointer + 1
                else:
                    mergedArray.append(B[arr2Pointer])
                    arr2Pointer = arr2Pointer + 1
            if(totalLeng % 2 == 0):
                # Length is odd
                median = (float(mergedArray[mid-1]) + mergedArray[mid]) / 2
                return median
            else:
                median = float(mergedArray[mid]) 
                return median

Solution.findMedianSortedArrays(A, B)