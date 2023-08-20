# O(n)

# set pointer at initial index 0 and last index len(n)-1
# we set leftmax and rightmax as initial and last value
# if leftmax is less than rightmax:
# increase the left pointer then leftmax is the max between currentmax and height[left]
# same for right pointer
# return the result

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
