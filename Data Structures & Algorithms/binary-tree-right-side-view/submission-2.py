from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        visible = []
        q = deque([root])
        while q:
            cur_level_size = len(q)
            for i in range(cur_level_size):
                cur_node = q.popleft()
                if i == cur_level_size - 1:
                    visible.append(cur_node.val)

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

        return visible