# O(mlogn)

# initialize list comprehension of (position, speed) using zip to combine both lists
# initialize list for stack

# we need to sort the list comprehension in reverse order
# iterating through the loop
# appending each velocity i.e distance=target-position/ speed
# if previous stack has velocity less than its previous the become a fleet
# hence pop the previous one
# return total length of stack after completing loop

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(Solution().carFleet(target, position, speed))
