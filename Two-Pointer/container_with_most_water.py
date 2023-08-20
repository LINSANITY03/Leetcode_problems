# O(n)

# initialize two pointer from index 0 and last
# set result as 0 since we are comparing the max area
# while left pointer is less than right pointer
# to check area, we need to find breadth and height
# breadth = right - left
# minimum height between left and right height
# then calculate area = length * breadth then compare with res

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1

        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))
