import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones] # Convert min heap to max heap by storing additive inverses

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            largest = heapq.heappop(max_heap)
            second_largest = heapq.heappop(max_heap)
            if largest != second_largest:
                heapq.heappush(max_heap, largest - second_largest)

        if len(max_heap) == 0:
            return 0
        return -max_heap[0] # Convert back