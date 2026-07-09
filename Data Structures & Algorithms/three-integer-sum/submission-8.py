from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i] # a + b + c = 0 -> b + c = -a
            left, right = i + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res