import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_max_heap = [(-freq, task) for task, freq in Counter(tasks).items()]
        heapq.heapify(task_max_heap)

        time = 0
        pending_tasks = deque([])

        while task_max_heap or pending_tasks:
            if pending_tasks and pending_tasks[0][1] == time:
                heapq.heappush(task_max_heap, pending_tasks.popleft()[0])

            if not task_max_heap:
                leftmost = pending_tasks.popleft()
                heapq.heappush(task_max_heap, leftmost[0])
                time = leftmost[1]
            else:
                heap_first = heapq.heappop(task_max_heap)
                if -heap_first[0] > 1:
                    # Additive inverses are stored, so heap_first[0] + 1 moves the count closer to 0.
                    heap_first_updated = (heap_first[0] + 1, heap_first[1])
                    task_reset_time = time + n + 1
                    pending_tasks.append((heap_first_updated, task_reset_time))

                time += 1

        return time