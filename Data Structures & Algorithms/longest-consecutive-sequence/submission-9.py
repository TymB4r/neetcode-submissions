from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_sequence_len = 0
                i = 0

                while (num + i) in nums_set:
                    curr_sequence_len += 1
                    i += 1

                max_sequence_len = max(max_sequence_len, curr_sequence_len)

        return max_sequence_len