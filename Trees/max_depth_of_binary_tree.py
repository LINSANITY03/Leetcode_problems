from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# RECURSIVE DFS
# check if the node has an value
# simple dfs
# for every iteration we add value 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ITERATIVE DFS
# when we do an iterative method we need some kind of stack or queue.
# initially we add root and depth 1 in the stack
# since we are going to increase the depth we initialize as 0.
# while we have value in stack.
# we pop the value from the stack into parameter node and depth.
# if there is any node, we take the max of current_Res and depth
# after that we append left node and right node with depth + 1.
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


# BFS
# intialize the deque structure and initially add the root node
# since we are going to pop the value from the deque and iterate on it
# initiate the level as 0
# while there are value in queue
# pop the leftmost value and if there exist a left node append it same for right.
# increase level 1 by each iteration
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
