# create a empty list for returning final value and for subset
# send initial index 0 as parameters
# if the index is equal to length of s then return the subset copy
# else loop the input from i
# if the current str is palindrome then append the palindrome part to subset and backtrack by increasing index
# then pop the value
# to find the palindrome part
# we need to make sure that the first and last value if equal until left and right is same
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


s = "aab"
print(Solution().partition(s))
