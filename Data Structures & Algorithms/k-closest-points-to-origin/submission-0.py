from typing import List
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)

            heapq.heappush(max_heap, (-distance, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [x for _, x in max_heap]