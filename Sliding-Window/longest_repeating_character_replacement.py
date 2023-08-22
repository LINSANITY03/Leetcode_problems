# initialize hashmap to count the occurence of each character
# initialize maxf to find max substring with k replacement
# left pointer at initial index
# right pointer is going through every single position in s

# count the occurence of each element s[r]
# then calculate maximum size of the window
# current window - max occurence is greater than k
# it means that we need to replace more than k number
# hence, current window is not valid
# release the left side of the window and update the left pointer

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
