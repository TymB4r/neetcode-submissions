import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(eating_speed: int) -> int:
            hours_needed = 0

            for pile in piles:
                hours_needed += math.ceil(pile / eating_speed)

            return hours_needed

        min_check, max_check = 1, max(piles)

        min_time = float('inf')
        while min_check <= max_check:
            mid = (min_check + max_check) // 2

            hours = time(mid)
            if hours <= h:
                min_time = min(min_time, mid)
                max_check = mid - 1
            else:
                min_check = mid + 1

        return min_time