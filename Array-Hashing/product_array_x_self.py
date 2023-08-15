# O(n) solution

# we have to initialize the array size similar to input
# prefix and postfix is the main idea
# if no prefix == 1 else prefix * current = list[current_index]
# if no postfix == 1 else postfix * current_list[current] = list[current_index]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
