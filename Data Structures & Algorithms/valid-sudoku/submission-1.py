from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        def check_rows() -> bool:
            for row in range(N):
                seen = set()
                for col in range(N):
                    c = board[row][col]
                    if c != ".":
                        if c in seen:
                            return False
                        seen.add(c)
            return True

        def check_columns() -> bool:
            for col in range(N):
                seen = set()
                for row in range(N):
                    c = board[row][col]
                    if c != ".":
                        if c in seen:
                            return False
                        seen.add(c)
            return True

        def check_boxes() -> bool:
            for left_start in range(0, N, N // 3):
                for top_start in range(0, N, N // 3):

                    seen = set()
                    for i in range(left_start, left_start + N // 3):
                        for j in range(top_start, top_start + N // 3):
                            c = board[i][j]
                            if c != ".":
                                if c in seen:
                                    return False
                                seen.add(c)
            return True

        if check_rows() and check_columns() and check_boxes():
            return True
        return False