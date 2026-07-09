class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')': '(', '}': '{', ']': '['
        }

        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if not stack or stack.pop() != match[c]:
                    return False

        if not stack:
            return True
        return False