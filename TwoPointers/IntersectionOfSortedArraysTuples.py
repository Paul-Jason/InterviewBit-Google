class Solution:
    def intersect(self, A, B):
        lenA = len(A)
        lenB = len(B)
        result = []
        lastJ = 0
        if(lenA > lenB):
            for i in range(0,lenB):
                eleB = B[i]
                foundAt = self.binarySearch(A,lastJ,lenA-1,eleB)
                if(foundAt != -1):
                    result.append(eleB)
                    lastJ = foundAt + 1                            
            return result
        else:
            for i in range(0,lenA):
                eleA = A[i]
                foundAt = self.binarySearch(B,lastJ,lenB-1,eleA)
                if(foundAt != -1):
                    result.append(eleA)
                    lastJ = foundAt + 1
            return result

    def binarySearch(self, arr,l,r,ele):
        if(r >= l):
            mid = (l+ r) // 2
            if(arr[mid] == ele):
                return mid
            else:
                if(arr[mid] < ele):
                    return self.binarySearch(arr,mid+1,r,ele)
                else:
                    return self.binarySearch(arr,l,mid-1,ele)
        else:
            return -1

A = ( 1, 3, 8, 10, 13, 13, 16, 16, 16, 18, 21, 23, 24, 31, 31, 31, 33, 35, 35, 37, 37, 38, 40, 41, 43, 47, 47, 48, 48, 52, 52, 53, 53, 55, 56, 60, 60, 61, 61, 63, 63, 64, 66, 67, 67, 68, 69, 71, 80, 80, 80, 80, 80, 80, 81, 85, 87, 87, 88, 89, 90, 94, 95, 97, 98, 98, 100, 101 )
B = ( 5, 7, 14, 14, 25, 28, 28, 34, 35, 38, 38, 39, 46, 53, 65, 67, 69, 70, 78, 82, 94, 94, 98 )
Solution().intersect(A,B)

