# this is a classic memoization to save the result when same input occur
# we can know the if there is only 2 stairs it takes 2 output,
# 1-1, 2 steps
# for every new stairs we add the previous value
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one


n = 2
print(Solution().climbStairs(n))
