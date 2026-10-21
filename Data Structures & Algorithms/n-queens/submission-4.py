from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid_diagonally(row: int, col: int) -> bool:
            differences = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dx, dy in differences:
                temp_row, temp_col = row, col
                while 0 <= temp_row < n and 0 <= temp_col < n:
                    if (temp_row, temp_col) in queen_positions:
                        return False
                    temp_row, temp_col = temp_row + dx, temp_col + dy
            return True

        queen_positions = []
        result_not_converted = []
        free_cols = {x for x in range(n)}

        def backtrack(row: int):
            nonlocal result_not_converted, queen_positions, free_cols
            if row == n:
                result_not_converted.append(queen_positions.copy())
                return

            # An hour spent looking why columns disappeared only to realize iterating over free_cols iterates through the reference, not a copy ;)
            for col in free_cols.copy():
                if is_valid_diagonally(row, col):
                    queen_positions.append((row, col))
                    free_cols.remove(col)
                    backtrack(row + 1)
                    free_cols.add(col)
                    queen_positions.remove((row, col))

        backtrack(0)

        result = []
        for layout in result_not_converted:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for row, col in layout:
                board[row][col] = 'Q'
            for row in range(n):
                board[row] = ''.join(board[row])

            result.append(board)

        return result