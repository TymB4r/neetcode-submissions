from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n - 1
        max_to_left, max_to_right = height[0], height[-1]
        area = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                max_to_left = max(max_to_left, height[left])
                area += max_to_left - height[left]
            else:
                right -= 1
                max_to_right = max(max_to_right, height[right])
                area += max_to_right - height[right]

        return area