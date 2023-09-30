# we need to sort the list because we need to check the next element to skip it
# we start the backtrack with initial pointer and empty list as subset
# if the subset length is equal to list number return the append the copy of subset to result
#  first we need to include the number into the empty subset
# append the nums[i] into the subset
# then backtrack with increasing i by 1 and return the latest subset
# then pop the value as a standard backtrack
# after popping the value check if the length is not greater than nums and next duplicate element
# if they are just shift the pointer to next i
# then return the subset
# this makes the length of subset equal to nums without adding any new value
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))
