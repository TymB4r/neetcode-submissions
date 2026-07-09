from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_to_left, max_to_right = height[l], height[r]
        area = 0
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_to_left = max(max_to_left, height[l])
                area += max_to_left - height[l]
            else:
                r -= 1
                max_to_right = max(max_to_right, height[r])
                area += max_to_right - height[r]

        return area