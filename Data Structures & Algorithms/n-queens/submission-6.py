from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid_diagonally(row: int, col: int) -> bool:
            return all(
                abs(row - r) != abs(col - c)
                for r, c in queen_positions
            )

        queen_positions = []
        placements = []
        free_cols = set(x for x in range(n))

        def backtrack(row: int):
            if row == n:
                placements.append(queen_positions.copy())
                return

            # An hour spent looking why columns disappeared only to realize iterating over free_cols iterates through the reference, not a copy ;)
            for col in free_cols.copy():
                if is_valid_diagonally(row, col):
                    queen_positions.append((row, col))
                    free_cols.remove(col)
                    backtrack(row + 1)
                    free_cols.add(col)
                    queen_positions.pop()

        backtrack(0)

        result = []
        for layout in placements:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for row, col in layout:
                board[row][col] = 'Q'
            for row in range(n):
                board[row] = ''.join(board[row])

            result.append(board)

        return result
