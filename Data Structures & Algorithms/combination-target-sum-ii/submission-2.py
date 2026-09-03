from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        elements = []
        for ele in sorted(candidates):
            if elements and elements[-1][0] == ele:
                elements[-1][1] += 1
            else:
                elements.append([ele, 1])

        result = []
        def backtrack(cur_sum: int, ele_idx: int, cur_path: List[int]) -> None:
            if cur_sum == target:
                result.append(cur_path.copy())
                return
            if ele_idx == len(elements) or cur_sum > target:
                return

            if elements[ele_idx][1] > 0:
                cur_path.append(elements[ele_idx][0])
                elements[ele_idx][1] -= 1
                backtrack(cur_sum + elements[ele_idx][0], ele_idx, cur_path)
                elements[ele_idx][1] += 1
                cur_path.pop()
            backtrack(cur_sum, ele_idx + 1, cur_path)

        backtrack(0, 0, [])
        return result