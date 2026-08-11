from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur_max_of_children(start: Optional[TreeNode], curr_depth: int) -> int:
            if not start:
                return curr_depth

            return max(recur_max_of_children(start.left, curr_depth + 1), recur_max_of_children(start.right, curr_depth + 1))

        if not root: return 0
        return max(recur_max_of_children(root.left, 1), recur_max_of_children(root.right, 1))