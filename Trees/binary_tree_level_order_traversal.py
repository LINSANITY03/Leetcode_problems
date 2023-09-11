# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# this is a example of classic bfs
# we traverse throught each node and collect the value on the queue
# if their is root node we append the value to the queue
# then we pop the value append on the list
# we need to check if the node has any left, right
# append those value to queue as well


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
