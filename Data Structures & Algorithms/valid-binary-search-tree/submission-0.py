from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse_with_bounds(node: Optional[TreeNode], left_bound: int | float, right_bound: int | float) -> bool:
            if not node:
                return True
            if not (left_bound < node.val < right_bound):
                return False

            return traverse_with_bounds(node.left, left_bound, node.val) and traverse_with_bounds(node.right, node.val, right_bound)
        return traverse_with_bounds(root, -float('inf'), float('inf'))