from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def backtrack(cells_seen: set[tuple[int, int]], cur_row: int, cur_col: int, idx_in_word: int) -> bool:
            if idx_in_word == len(word):
                return True

            if (cur_row < 0 or cur_row >= len(board) or cur_col < 0 or cur_col >= len(board[0])
                    or ((cur_row, cur_col) in cells_seen) or board[cur_row][cur_col] != word[idx_in_word]):
                return False
            cells_seen.add((cur_row, cur_col))
            for dr, dc in directions:
                if backtrack(cells_seen, cur_row + dr, cur_col + dc, idx_in_word + 1):
                    return True
            cells_seen.remove((cur_row, cur_col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(set(), row, col, 0):
                    return True

        return False