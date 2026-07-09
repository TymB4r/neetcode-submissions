from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        starting_points = set()

        for num in nums:
            if num - 1 not in nums_set:
                starting_points.add(num)

        max_len = 0
        for start in starting_points:
            curr_len = 0
            i = 0

            while (start + i) in nums_set:
                curr_len += 1
                i += 1
            max_len = max(max_len, curr_len)

        return max_len