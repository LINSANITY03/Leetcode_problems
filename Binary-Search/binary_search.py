# O(logn)

# simple binary search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))
