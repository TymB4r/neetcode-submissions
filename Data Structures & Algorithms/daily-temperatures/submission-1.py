from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                diff = idx - stack.pop()[0] # stack.pop()[0] = idx - diff
                res[idx - diff] = diff

            stack.append((idx, temp))

        return res