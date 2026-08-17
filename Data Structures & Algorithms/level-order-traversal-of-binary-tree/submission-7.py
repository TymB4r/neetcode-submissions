from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        level_order_list = []
        level_size = 1
        while q:
            cur_level = []

            # level_size is changed inside the loop to prepare it for the next level,
            # but range(level_size) still does the original amount of iterations
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur_level.append(cur_node.val)

                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)

            level_order_list.append(cur_level)

        return level_order_list