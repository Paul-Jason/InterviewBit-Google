class Solution:
    def intersect(self, A, B):
        lenA = len(A)
        lenB = len(B)
        result = []
        if(lenA > lenB):
            for i in range(0,lenB):
                eleB = B[i]
                foundAt = self.binarySearch(A,0,lenA-1,eleB)
                if(foundAt != -1):
                    result.append(eleB)
                    A.remove(eleB)
            return result
        else:
            for i in range(0,lenA):
                eleA = A[i]
                foundAt = self.binarySearch(B,0,lenB-1,eleA)
                if(foundAt != -1):
                    result.append(eleA)
                    B.remove(eleA)
            return result

    def binarySearch(self, arr,l,r,ele):
        mid = (l+r) // 2
        if(arr[mid] == ele):
            return mid
        else:
            if(l == r):
                return -1
            if(arr[mid] < ele):
                self.binarySearch(arr,mid,r,ele)
            else:
                self.binarySearch(arr,l,mid,ele)

A = (1,2,3,3,4,5,6)
B = (3,5)
Solution().intersect(A,B)

