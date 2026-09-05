from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        elements = sorted(nums)
        result = []

        def backtrack(cur_idx: int, cur_subset: List[int]):
            if cur_idx == len(elements):
                result.append(cur_subset.copy())
                return

            # take current element
            backtrack(cur_idx + 1, cur_subset + [elements[cur_idx]])

            # don't take current value at all
            cur_num = elements[cur_idx]

            while cur_idx < len(elements) and elements[cur_idx] == cur_num:
                cur_idx += 1

            backtrack(cur_idx, cur_subset)

        backtrack(0, [])
        return result