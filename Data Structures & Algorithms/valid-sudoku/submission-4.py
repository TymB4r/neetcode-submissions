from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ Works for N divisible by 3"""
        N = len(board) # The board is an NxN matrix

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        squares = [[set() for _ in range(N // 3)] for _ in range(N // 3)]
        scale = N // 3  # Box : single cell
        for r in range(N):
            for c in range(N):
                char = board[r][c]
                if char == '.':
                    continue
                if (char in rows[r]) or (char in cols[c]) or (char in squares[r // scale][c // scale]):
                    return False

                rows[r].add(char)
                cols[c].add(char)
                squares[r // scale][c // scale].add(char)

        return True