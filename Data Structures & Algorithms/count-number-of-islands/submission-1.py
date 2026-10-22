from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = grid.copy()
        ROWS, COLS = len(grid_copy), len(grid_copy[0])
        found = 0

        def traverse(row: int, col: int):
            grid_copy[row][col] = "0"
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS) and grid_copy[nr][nc] == "1":
                    traverse(nr, nc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid_copy[row][col] == "0":
                    continue

                found += 1
                traverse(row, col)

        traverse(0, 0)
        return found