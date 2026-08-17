from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_list = []

        def traverse(root: Optional[TreeNode], cur_height: int) -> None:
            nonlocal level_order_list
            if not root:
                return

            if cur_height >= len(level_order_list):
                level_order_list.append([])
            level_order_list[cur_height].append(root.val)

            traverse(root.left, cur_height + 1)
            traverse(root.right, cur_height + 1)

        traverse(root, 0)
        return level_order_list