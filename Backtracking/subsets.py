# we need to initialize a list which we return in result and a subset for every iteration
# we start with iteration at index 0
# we append nums[i] to subset then we backtrack by incremeneting the index
# we check if the subset is equal to nums the return subset
# then we pop previous set such that we can have ttwo possibilities
# adding a number and not adding a number
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
