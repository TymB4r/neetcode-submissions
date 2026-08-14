from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and not q) or (q and not p):
            return False

        if p.val != q.val: # From previous condition: p and q == True
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)