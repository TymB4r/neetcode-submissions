from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.recur(root, 1)
        return self.max_depth

    def recur(self, start: Optional[TreeNode], curr_depth: int) -> None:
        if not start:
            return
        self.max_depth = max(self.max_depth, curr_depth)

        self.recur(start.left, curr_depth + 1)
        self.recur(start.right, curr_depth + 1)