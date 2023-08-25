# O(n)

# first we initalize stack and minstack as a list
# we append the val to stack and check the minimum value in minstack
# we pop value from both stack and minstack
# get the last value from stack as top
# get the last value from minstack as getMin

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[], [-2], [0], [-3], [], [], [], []]

minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
