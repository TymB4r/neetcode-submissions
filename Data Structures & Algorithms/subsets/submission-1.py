from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(cur_set: List[int], idx: int) -> None:
            if idx < n:
                backtrack(cur_set, idx+1)
                backtrack(cur_set+[nums[idx]], idx+1)
            elif len(result) < 2**n:
                result.append(cur_set)

        backtrack([], -1)
        return result