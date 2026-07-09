from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(eating_speed: int) -> int:
            total_time = 0

            for pile in piles:
                total_time += ceil(pile / eating_speed)

            return total_time

        left_time, right_time = 1, max(piles)

        min_time = float('inf')
        while left_time <= right_time:
            mid = (left_time + right_time) // 2

            if hours_needed(mid) <= h:
                min_time = min(min_time, mid)
                right_time = mid - 1
            else:
                left_time = mid + 1

        return left_time