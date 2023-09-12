# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs
# initialize none as rightside
# pop every item then replace the rightside
# after iteration is completed check for result and send either val or none


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
