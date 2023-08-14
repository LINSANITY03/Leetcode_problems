class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if both string has equal length else they are different string
        if len(s) != len(t):
            return False

        # initialize two dictionary for s and t string
        countS, countT = {}, {}

        # increment a component if it exist .get(component, 0)
        # either get value of s[i] or use 0 as a value
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # return true or false by comparing those two dictionary
        return countS == countT


s, t = "anagram", "nagaram"
print(Solution().isAnagram(s, t))
