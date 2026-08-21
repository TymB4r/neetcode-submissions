class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_path_sum = float('-inf')

        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum
            if not node:
                return 0

            left_path = traverse(node.left)
            right_path = traverse(node.right)

            max_path_sum = max(max_path_sum, node.val, node.val + left_path, node.val + right_path, node.val + right_path + left_path)
            return node.val + max(0, left_path, right_path)

        traverse(root)
        return max_path_sum