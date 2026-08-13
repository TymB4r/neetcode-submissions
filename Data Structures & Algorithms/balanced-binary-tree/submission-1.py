from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def recur(start: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not start:
                return 0

            left_height = recur(start.left)
            right_height = recur(start.right)
            if abs(left_height - right_height) > 1:
                balanced = False

            return 1 + max(left_height, right_height)

        recur(root)
        return balanced