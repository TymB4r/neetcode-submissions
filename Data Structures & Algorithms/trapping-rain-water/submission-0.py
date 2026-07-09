from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        biggest_to_right = [0] * n
        cur_biggest = 0
        for i in range(n - 1, -1, -1):
            biggest_to_right[i] = cur_biggest
            cur_biggest = max(height[i], cur_biggest)

        biggest_to_left = [0] * n
        cur_biggest = 0
        for i in range(n):
            biggest_to_left[i] = cur_biggest
            cur_biggest = max(height[i], cur_biggest)

        trapped = 0
        for i in range(n):
            trapped += max(0, min(biggest_to_right[i], biggest_to_left[i]) - height[i])

        return trapped