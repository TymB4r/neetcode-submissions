from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def traverse(node: Optional[TreeNode]):
            nonlocal result
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return ','.join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serialized = data.split(',')
        idx = 0
        def build() -> Optional[TreeNode]:
            nonlocal idx
            if idx >= len(serialized) or serialized[idx] == 'N':
                idx += 1
                return None

            node = TreeNode(int(serialized[idx]))
            idx += 1
            node.left = build()
            node.right = build()
            return node

        root = build()
        return root