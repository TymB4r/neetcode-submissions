from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        right_bound = []
        cur_max_to_right = -float('inf')
        for i in range(n - 1, -1, -1):
            cur_height = height[i]
            if cur_height > cur_max_to_right:
                right_bound.append(i)
                cur_max_to_right = cur_height

        left_bound = []
        cur_max_to_left = -float('inf')
        for i in range(n):
            cur_height = height[i]
            if cur_height > cur_max_to_left:
                left_bound.append(i)
                cur_max_to_left = cur_height
        left_bound.reverse()

        print(right_bound)
        print(left_bound)

        area = 0
        cur_left_bound, cur_right_bound = 0, height[right_bound[-1]]
        right_bound_change_place = right_bound.pop()
        for i in range(n):
            if right_bound and i > right_bound_change_place:
                right_bound_change_place = right_bound.pop()
                cur_right_bound = height[right_bound_change_place]
            if left_bound and i == left_bound[-1]:
                cur_left_bound = height[left_bound.pop()]

            area += max(0, min(cur_right_bound, cur_left_bound) - height[i])

        return area