# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first, we need to check if the tree has no root
# to invert the tree, the logic behind is recursion
# we swap the root.left to root.right and reverse
# then we use to recursive calls, one for left and other for right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap the children
        root.left, root.right = root.right, root.left

        # make 2 recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
