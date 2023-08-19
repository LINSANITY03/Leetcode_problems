# initialize two-pointer with indexing 0 and -1
# while left pointer is less than right pointer
# check sum is equal to target then return both element index
# else if less add left pointer or sub right pointer
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]

            if total < target:
                l += 1
            else:
                r -= 1
