from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_path_sum = float('-inf')

        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum
            if not node:
                return 0

            left_path = traverse(node.left)
            right_path = traverse(node.right)

            cur_max_path_sum = max(node.val, node.val + left_path, node.val + right_path, node.val + right_path + left_path)
            max_path_sum = max(max_path_sum, cur_max_path_sum)

            return node.val + max(0, left_path, right_path)

        traverse(root)
        return max_path_sum