import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                seen.append(int(token))
            else:
                last = int(seen.pop())

                if token == "+":
                    seen[-1] += last
                elif token == "-":
                    seen[-1] -= last
                elif token == "*":
                    seen[-1] *= last
                elif token == "/":
                    if seen[-1] / last < 0:
                        seen[-1] = math.ceil(seen[-1] / last)
                    else:
                        seen[-1] = math.floor(seen[-1] / last)
        return seen[-1]