class Solution:
    def f(self, A, n):
        if n == len(A):
            return [list(A)]
        else:
            ans = []
            s = set()
            ans += self.f(A, n + 1)
            s.add(A[n])
            for i in range(n+1, len(A)):
                if A[i] not in s:
                    A[n], A[i] = A[i], A[n]
                    ans += self.f(A, n + 1)
                    A[n], A[i] = A[i], A[n]
                    s.add(A[i])
            return ans

    # @return a list of list of integers
    def permute(self, A):
        return self.f(A, 0)

A = [1,2,3]
Solution().permute(A)