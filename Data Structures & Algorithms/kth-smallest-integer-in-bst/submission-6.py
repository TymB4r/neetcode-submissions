from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int | None:
        # The solution relies on the fact, that the inorder traversal for the binary search tree is increasing
        processed_nodes = 0
        kth_smallest_value = None

        def traverse(node: Optional[TreeNode]) -> None:
            nonlocal processed_nodes, kth_smallest_value
            if not node or processed_nodes >= k:
                return

            traverse(node.left)
            if processed_nodes >= k:
                return
            processed_nodes += 1

            if processed_nodes == k:
                kth_smallest_value = node.val

            traverse(node.right)

        traverse(root)
        return kth_smallest_value