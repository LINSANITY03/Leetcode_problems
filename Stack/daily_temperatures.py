# initialize the list as [0] * length of temperatures since we want 0 as default value
# initialize stack as a list

# for each enumeration of temperatures
# append the (current_temp_value, index) to the stack
# if stack is not empty and current_temp_value is greater than previous stack value
# we need to pop previous first
# then, update res[prev_index] = current_index - previous_index (index, time to get warmer)
# until there are value less than current_value

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
