from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1] # We make the result 1-indexed
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1