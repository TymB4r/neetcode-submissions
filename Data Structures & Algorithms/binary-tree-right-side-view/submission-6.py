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
            visible.append(q[-1].val) # The rightmost node of each level is always the visible one
            cur_level_size = len(q)
            for _ in range(cur_level_size):
                cur_node = q.popleft()

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

        return visible