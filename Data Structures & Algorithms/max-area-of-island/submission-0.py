from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        grid_copy = [row.copy() for row in grid]

        def traverse(row: int, col: int):
            q = deque([(row, col)])
            grid_copy[row][col] = "0"
            cur_area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and grid_copy[nr][nc] == 1:
                        cur_area += 1
                        grid_copy[nr][nc] = 0
                        q.append((nr, nc))

            return cur_area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid_copy[row][col] == 1:
                    max_area = max(max_area, traverse(row, col))

        return max_area