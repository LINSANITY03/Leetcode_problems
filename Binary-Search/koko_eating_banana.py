# initiate the pointer as 1hour and maxhour for left, right pointer
# we know min result will be max of the number
# while using binary search
# we need to calculate totaltime should be less than h
# if it is compare with result and again try to find more small number
# if it is small right = k -1
# else left = k + 1

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = l + ((r - l) // 2)

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


piles = [3, 6, 7, 11]
h = 8

print(Solution().minEatingSpeed(piles, h))
