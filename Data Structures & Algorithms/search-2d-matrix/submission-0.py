from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix) - 1

        while row_left <= row_right:
            row_mid = (row_left + row_right) // 2

            if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
                break
            elif matrix[row_mid][0] < target:
                row_left = row_mid + 1
            else:
                row_right = row_mid - 1

        col_left, col_right = 0, len(matrix[row_mid]) - 1

        while col_left <= col_right:
            col_mid = (col_left + col_right) // 2

            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][col_mid] < target:
                col_left = col_mid + 1
            else:
                col_right = col_mid - 1
                
        return False