# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node: TreeNode, cur_max_node: int) -> int:
            if not node:
                return 0

            if node.val >= cur_max_node:
                return 1 + traverse(node.left, node.val) + traverse(node.right, node.val)
            else:
                return traverse(node.left, cur_max_node) + traverse(node.right, cur_max_node)

        return traverse(root, root.val)