# initialize a stack and result list
# function backtracking has 3 parts

# first part, if open and close brackets is equal to required n amount
# return the joined stack and append to res

# second part, if open brackets is less than required n amount
# append open brackets to the stack and backtrack using +1 amount of open brackets
# then pop the stack

# third part, if closed brackets is less than open brackets
# append closed brackets to the stack and backtrack using +1 amount of closed brackets
# then pop the stack

# always check priority is given to open brackets than closed
# first open brackets must be greater than closed

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


n = 3
print(Solution().generateParenthesis(n))
