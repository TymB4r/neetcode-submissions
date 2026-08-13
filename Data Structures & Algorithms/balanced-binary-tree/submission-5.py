from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(start: Optional[TreeNode]) -> int:
            if not start:
                return 0

            left_height = recur(start.left)
            if left_height == -1:
                return -1
            right_height = recur(start.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        if recur(root) == -1:
            return False
        return True