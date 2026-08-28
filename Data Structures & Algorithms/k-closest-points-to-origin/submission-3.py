from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            distance_squared = point[0]**2 + point[1]**2 # dist1^2 < dist2^2 ==> dist1 < dist2 

            heapq.heappush(max_heap, (-distance_squared, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [x for _, x in max_heap]