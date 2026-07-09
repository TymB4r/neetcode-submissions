from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        max_time = 0

        for curr_pos, curr_speed in sorted(zip(position, speed), reverse=True):
            curr_time = (target - curr_pos) / curr_speed
            if curr_time > max_time:
                fleets += 1
                max_time = curr_time

        return fleets