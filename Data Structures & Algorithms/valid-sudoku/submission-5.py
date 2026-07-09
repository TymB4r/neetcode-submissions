from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board) # The board is an NxN matrix

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        squares = [set() for _ in range(N)]
        scale = N // 3  # Box : single cell
        for r in range(N):
            for c in range(N):
                char = board[r][c]
                box_idx = r // scale * 3 + c // scale
                if char == '.':
                    continue
                if (char in rows[r]) or (char in cols[c]) or (char in squares[box_idx]):
                    return False

                rows[r].add(char)
                cols[c].add(char)
                squares[box_idx].add(char)

        return True