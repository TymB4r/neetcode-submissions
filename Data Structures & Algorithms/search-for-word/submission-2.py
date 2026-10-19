from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(cells_seen: List[tuple[int, int]], cur_row: int, cur_col: int, idx_in_word: int) -> bool:
            if (cur_row < 0 or cur_row >= len(board) or cur_col < 0 or cur_col >= len(board[0])
                or ((cur_row, cur_col) in cells_seen) or board[cur_row][cur_col] != word[idx_in_word]):
                return False

            return (
                idx_in_word == len(word) - 1 or
                backtrack(cells_seen + [(cur_row, cur_col)], cur_row + 1, cur_col, idx_in_word + 1) or
                backtrack(cells_seen + [(cur_row, cur_col)], cur_row - 1, cur_col, idx_in_word + 1) or
                backtrack(cells_seen + [(cur_row, cur_col)], cur_row, cur_col + 1, idx_in_word + 1) or
                backtrack(cells_seen + [(cur_row, cur_col)], cur_row, cur_col - 1, idx_in_word + 1)
            )

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack([], row, col, 0):
                    return True

        return False