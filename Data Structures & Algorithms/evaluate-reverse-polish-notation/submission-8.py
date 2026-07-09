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
                # if token == "+":
                #     stack[-1] += last
                #
                # elif token == "-":
                #     stack[-1] -= last
                #
                # elif token == "*":
                #     stack[-1] *= last
                #
                # elif token == "/":
                #     if stack[-1] / last < 0:
                #         stack[-1] = math.ceil(stack[-1] / last)
                #     else:
                #         stack[-1] = math.floor(stack[-1] / last)

        return stack[-1]
