class Solution:

    def binarySearch(self, arr,l,r,ele):
        mid = (l+r) // 2
        if(arr[mid] == ele):
            return [mid]
        else:
            if(l == r):
                return [l,r]
            if(arr[mid] < ele):
                self.binarySearch(arr,mid,r,ele)
            else:
                self.binarySearch(arr,l,mid,ele)

    def searchForARange():


A = [5,7,7,8,8,10]
B =  
Solution().intersect(A,B)

