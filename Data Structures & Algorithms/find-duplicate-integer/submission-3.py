from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat the array like a linked list: each number is a pointer pointing to the next index
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        finder = 0
        while finder != slow:
            slow = nums[slow]
            finder = nums[finder]

        return finder