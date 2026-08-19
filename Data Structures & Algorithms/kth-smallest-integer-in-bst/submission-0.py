from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_traversed_count = 0
        kth_smallest_found = False
        kth_smallest = -1
        def traverse(node):
            nonlocal smallest_traversed_count, kth_smallest, kth_smallest_found
            if not node or kth_smallest_found:
                return

            traverse(node.left)
            smallest_traversed_count += 1
            if smallest_traversed_count == k:
                kth_smallest = node.val
                kth_smallest_found = True
            traverse(node.right)

        traverse(root)
        return kth_smallest