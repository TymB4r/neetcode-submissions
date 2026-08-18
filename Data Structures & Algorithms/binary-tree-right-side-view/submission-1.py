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
            visible.append(None)
            for _ in range(len(q)):
                node = q.popleft()
                visible[-1] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return visible