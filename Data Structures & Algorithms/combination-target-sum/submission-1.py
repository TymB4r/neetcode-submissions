from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        elements = sorted(nums)

        result = []

        def backtrack(cur_sum: int, ele_idx: int, cur_path: List[int]) -> None:
            if cur_sum == target:
                result.append(cur_path.copy())
                return
            if ele_idx == len(elements) or cur_sum > target:
                return

            cur_path.append(elements[ele_idx])
            backtrack(cur_sum + elements[ele_idx], ele_idx, cur_path)
            cur_path.pop()
            backtrack(cur_sum, ele_idx + 1, cur_path)

        backtrack(0, 0, [])
        return result