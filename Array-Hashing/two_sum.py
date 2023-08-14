# To find the index of two numbers that when added gives the target number

# Main Logic
# we find the target-current_value and if this is in the hasmap we return its value.
# else we append current-value with key and its index as pair
# ----> {key: pair} -- {current_value: index}

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[val] = i


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
