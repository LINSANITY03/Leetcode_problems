# O(n)

# first we must decalre a set variable, left pointer and the result
# loop every index
# while current char is in the set: remove the left pointer and increment by 1. Hence, the sliding window
# we need to add current right pointer value to the set
# update the result with right-left+1 length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
