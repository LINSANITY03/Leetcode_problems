# this is a floyds cycle technique of tortoise and hare problem
# first we start the classic hare and tortoise and get the value of nums[slow]

# we need to do it again such that there are no problem
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


nums = [2, 5, 9, 6, 9, 3, 8, 9, 9, 1]
print(Solution().findDuplicate(nums))
