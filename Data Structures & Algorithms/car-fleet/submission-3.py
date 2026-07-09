from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)
        fleets = 0
        max_time = 0
        for pos, spd in sorted(zip(position, speed), reverse=True):
            cur_time = (target - pos) / spd
            if cur_time > max_time:
                fleets += 1
                max_time = cur_time

        return fleets