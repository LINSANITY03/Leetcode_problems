# O(n)

# initialize a list for storing elements of tokens as a stack
# for each item in token
# if it is a operator then pop the element of last two stack and perform operations
# else append to the stack
# return the last item of stack to user

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(Solution().evalRPN(tokens))
