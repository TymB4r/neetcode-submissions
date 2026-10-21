from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid_diagonally(row: int, col: int) -> bool:
            return (
                    row - col not in occupied_diff_diagonals
                    and row + col not in occupied_sum_diagonals
            )

        def build_board(layout: List[tuple[int, int]]) -> List[str]:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for row, col in layout:
                board[row][col] = 'Q'

            return [''.join(board[row]) for row in range(n)]

        queen_positions = []
        occupied_diff_diagonals = set()
        occupied_sum_diagonals = set()

        result = []
        free_cols = set(range(n))

        def backtrack(row: int):
            if row == n:
                result.append(build_board(queen_positions))
                return

            # Iterate over the copy of free_cols, because the recursive calls might change the desired iteration set
            for col in free_cols.copy():
                if is_valid_diagonally(row, col):
                    queen_positions.append((row, col))
                    occupied_diff_diagonals.add(row - col)
                    occupied_sum_diagonals.add(row + col)
                    free_cols.remove(col)

                    backtrack(row + 1)

                    free_cols.add(col)
                    queen_positions.pop()
                    occupied_diff_diagonals.remove(row - col)
                    occupied_sum_diagonals.remove(row + col)

        backtrack(0)
        return result
