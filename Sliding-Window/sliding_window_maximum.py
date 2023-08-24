import collections

# O(n)
# initialize list to represent list of maximum number in sliding window
# we initialize a queue for setting the max in sliding window at partcular iteration
# initialize the left and right pointer at 0 since we are using while
# while right pointer is less than length of list (setting the boundary)
# then we need to add the current index to queue
# if there are value in queue and queue value is less than current, we pop the queue
# then insert current value
# if our window is out of bounds remove the leftmost value (end of cur iter)
# if our loop is equal to sliding wiwndow size 'k' then append the max value(leftmost) and increase
# left pointer by 1
# we need to increase r by 1 in every iteration


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
