# O(n)

# initialize maxArea as 0 and stack as list
# enumerate the heights to get value and its index
# we need to set starting index as i for each iteration
# check if stack and the top of stack height is greater than current
# if true pop the top of stack and calculate the max area using start index
# after wards check if there are value in stack
# these are sorted type so we can iterate and find max area using len heights as max

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
