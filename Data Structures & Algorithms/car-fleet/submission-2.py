from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def sort_accordingly(position, speed):
            zipped = list(zip(position, speed))
            zipped.sort(reverse=True)
            position, speed = zip(*zipped)
            position, speed = list(position), list(speed)
            return position, speed

        position, speed = sort_accordingly(position, speed)

        n = len(position)
        fleets = 1
        max_time = (target - position[0]) / speed[0]
        for i in range(1, n):
            cur_time = (target - position[i]) / speed[i]
            if cur_time > max_time:
                fleets += 1
                max_time = cur_time

        return fleets