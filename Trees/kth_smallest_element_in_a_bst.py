# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the left in a bst is the smallest element
# we create a stack
# add a pointer to the root
# while there is a valid node or else value on the stack
# append those value to the stack and forward the pointer to the leftnode
# get the smallest value first and increase the value of k


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if k == n:
                return curr.val
            curr = curr.right
