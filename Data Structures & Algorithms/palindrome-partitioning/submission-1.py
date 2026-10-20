from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def search(start: int) -> None:
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring == substring[::-1]:
                    path.append(substring)
                    search(end)
                    path.pop()

        search(0)
        return result
