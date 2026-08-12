from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def recur(start: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not start:
                return 0
            left_subtree_height = recur(start.left)
            right_subtree_height = recur(start.right)
            max_diameter = max(max_diameter, left_subtree_height + right_subtree_height)
            return 1 + max(left_subtree_height, right_subtree_height)

        recur(root)
        return max_diameter