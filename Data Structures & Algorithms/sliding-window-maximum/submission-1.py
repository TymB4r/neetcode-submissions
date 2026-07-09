from typing import List
from sortedcontainers import SortedDict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur_elements = SortedDict()

        res = []

        for i in range(k):
            if nums[i] not in cur_elements:
                cur_elements[nums[i]] = 1
            else:
                cur_elements[nums[i]] += 1
        res.append(cur_elements.peekitem(-1)[0])

        for i in range(k, len(nums)):
            cur_elements[nums[i - k]] -= 1
            if cur_elements[nums[i - k]] == 0:
                del cur_elements[nums[i - k]]

            if nums[i] not in cur_elements:
                cur_elements[nums[i]] = 1
            else:
                cur_elements[nums[i]] += 1

            res.append(cur_elements.peekitem(-1)[0])
            
        return res