from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        def recur(start):
            if not start:
                return 0
            nonlocal max_height
            left_subtree_size = recur(start.left)
            right_subtree_size = recur(start.right)
            max_height = max(max_height, left_subtree_size + right_subtree_size)
            return 1 + max(left_subtree_size, right_subtree_size)


        recur(root)
        return max_height