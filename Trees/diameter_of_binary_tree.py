# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# another dfs problem
# diameter is the longest path between any two nodes in a tree.
# simply we need find the max value of left+right node


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):

            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]
