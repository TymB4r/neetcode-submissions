from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = [row.copy() for row in grid]

        ROWS, COLS = len(grid_copy), len(grid_copy[0])
        island_count = 0

        def traverse(row: int, col: int):
            q = deque([(row, col)])
            #grid_copy[row][col] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and grid_copy[nr][nc] == "1":
                        grid_copy[nr][nc] = "0"
                        q.append((nr, nc))

        for row in range(ROWS):
            for col in range(COLS):
                if grid_copy[row][col] == "0":
                    continue

                island_count += 1
                traverse(row, col)

        return island_count