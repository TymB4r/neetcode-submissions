from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:  # Not <= because the array was ascending, meaning unique elements
                right = mid
            else:
                left = mid + 1

        if nums[left] == target:
            return left
        elif nums[left] < target and nums[-1] >= target:
            right = len(nums) - 1
        else:
            right, left = left, 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1