from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Create references
        if len(nums1) >= len(nums2):
            large, small = nums1, nums2
        else:
            large, small = nums2, nums1

        total_length = len(large) + len(small)
        half = total_length // 2
        small_left, small_right = 0, len(small) - 1

        # Partition invariant:
        # large: _ _ _ _ _ a | b _ _ _ _ _ _
        # small: _ _ _ c | d _ _ _ _
        # Where _ denotes other (insignificant) elements of the array
        # And | denotes the partition point, where a <= d and c <= b
        # Only one such case is possible, as the arrays taken separately are strictly increasing.
        while True:
            small_mid = (small_left + small_right) // 2

            a_idx = half - small_mid - 2
            a = -float('inf') if a_idx < 0 else large[a_idx]
            b = float('inf') if a_idx + 1 >= len(large) else large[a_idx + 1]

            c = -float('inf') if small_mid < 0 else small[small_mid]
            d = float('inf') if small_mid + 1 >= len(small) else small[small_mid + 1]

            if a <= d and c <= b:
                if total_length % 2 == 1:
                    return float(min(b, d))
                else:
                    return (max(a, c) + min(b, d)) / 2
            if c > b:
                small_right = small_mid - 1
            else:
                small_left = small_mid + 1