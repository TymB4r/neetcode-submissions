class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = []
        path = []

        def build(idx: int) -> None:
            if idx == len(digits):
                result.append("".join(path.copy()))
                return
            for let in digit_to_letters[digits[idx]]:
                path.append(let)
                build(idx + 1)
                path.pop()


        build(0)
        return result