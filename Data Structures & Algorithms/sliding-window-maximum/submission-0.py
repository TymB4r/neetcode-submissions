from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur_elements = SortedList()

        res = []

        for i in range(k):
            cur_elements.add(nums[i])
        res.append(cur_elements[-1])

        for i in range(k, len(nums)):
            cur_elements.remove(nums[i-k])
            cur_elements.add(nums[i])
            res.append(cur_elements[-1])

        return res