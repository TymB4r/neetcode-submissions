from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        found = 0

        def traverse(row: int, col: int):
            grid[row][col] = "0"
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == "1":
                    traverse(nr, nc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "0":
                    continue

                found += 1
                traverse(row, col)

        traverse(0, 0)
        return found