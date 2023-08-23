# first check if the target text is empty, return empty string ""
# initialize dictionary to count items in target s and current sliding window
# set current matching as have and need as total t length
# current sliding window pointer [-1, -1] and result length as max infinity
# starting pointer l,= 0
# for loop as current right pointer
# we need to add s[right pointer] into the window dict
# after adding the element check if it is in count[currnt ele] = windows[current ele]
# if have==need:
# check current window length is than reslen then update
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""


s = "ADOBECODEBANC"
t = "ABC"

print(Solution().minWindow(s, t))
