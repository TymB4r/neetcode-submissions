import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                last = stack.pop()
                stack[-1] = (operations[token](stack[-1], last))

        return stack[-1]