# O(log n)

# initially, we assume the first element of the list as minimum value
# initiate the left and right pointer as 0, len(nums) - 1
# start binary search
#   if left value is less than right value means it is sorted array
#   check current result and current mid value
#   if not, start binary search
#   check current result
#   if mid value is greater than left value, then we need to search right most value
#   hence, left pointer= mid + 1 else, right pointer= mid - 1

class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
