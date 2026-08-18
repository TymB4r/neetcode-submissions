# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node: TreeNode, cur_path_max: int) -> int:
            if not node:
                return 0

            new_max = max(node.val, cur_path_max)
            cur_node_good = int(node.val >= cur_path_max)
            return cur_node_good + traverse(node.left, new_max) + traverse(node.right, new_max)

        return traverse(root, root.val)