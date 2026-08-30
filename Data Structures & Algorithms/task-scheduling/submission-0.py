import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_freq = Counter(tasks)

        max_heap = []
        for task, freq in task_to_freq.items():
            max_heap.append((-freq, task))

        heapq.heapify(max_heap)


        total_time = 0
        queue = deque([])
        while queue or max_heap:
            if queue and queue[0][1] == total_time:
                heapq.heappush(max_heap, queue.popleft()[0])
            if not max_heap: # queue exists
                leftmost = queue.popleft()
                heapq.heappush(max_heap, (leftmost[0][0], leftmost[0][1]))
                total_time = leftmost[1]
            else:
                heap_first = heapq.heappop(max_heap)
                if -heap_first[0] > 1:
                    queue.append(((heap_first[0] + 1, heap_first[1]), total_time + n + 1))
                total_time += 1

        return total_time