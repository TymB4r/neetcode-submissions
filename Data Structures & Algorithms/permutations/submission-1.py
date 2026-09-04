from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(unused: List[int], cur_perm: List[int]) -> None:
            if not unused:
                result.append(cur_perm.copy())
                return

            for i in range(len(unused)):
                chosen = unused.pop(i)
                cur_perm.append(chosen)

                backtrack(unused, cur_perm)

                cur_perm.pop()
                unused.insert(i, chosen)

        backtrack(nums.copy(), [])
        return result