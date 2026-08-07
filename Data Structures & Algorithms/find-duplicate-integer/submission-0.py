from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        new_slow = 0

        while new_slow != slow:
            slow = nums[slow]
            new_slow = nums[new_slow]


        return new_slow