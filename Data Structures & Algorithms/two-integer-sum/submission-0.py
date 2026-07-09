class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, num in enumerate(nums):
            if target - num in complements:
                return [complements[target-num], i]
            complements[num] = i
        return [0, 0]