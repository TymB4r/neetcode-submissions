from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(start: Optional[TreeNode]):
            if not start.left and not start.right:
                return start

            if start.left:
                recur(start.left)
            if start.right:
                recur(start.right)
            start.left, start.right = start.right, start.left

            return start

        if not root:
            return None
        return recur(root)