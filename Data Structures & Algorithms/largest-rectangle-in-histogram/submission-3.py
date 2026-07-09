from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        right_bound = [0] * n
        for i in range(n - 1, -1, -1):
            cur_height = heights[i]
            while stack and cur_height <= heights[stack[-1]]:
                stack.pop()

            if not stack: # Current element <= every element to the right
                right_bound[i] = n - 1
            else: # cur_height > heights[stack[-1]]
                right_bound[i] = stack[-1] - 1
            stack.append(i)

        stack.clear()
        left_bound = [0] * n
        for i in range(n):
            cur_height = heights[i]
            while stack and cur_height <= heights[stack[-1]]:
                stack.pop()

            if not stack: # Current element <= every element to the left
                left_bound[i] = 0
            else: # cur_height > heights[stack[-1]]
                left_bound[i] = stack[-1] + 1
            stack.append(i)

        max_area = 0
        for i in range(n):
            max_area = max(max_area, (right_bound[i] - left_bound[i] + 1) * heights[i])

        return max_area