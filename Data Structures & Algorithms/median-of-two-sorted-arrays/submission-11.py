from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        long: _ _ _ _ _ a | b _ _ _ _ _ _
        short: _ _ _ c | d _ _ _ _
        Where _ denotes other (insignificant) elements of the array
        And | denotes the partition point, where a <= d and c <= b
        Only one such case is possible, as the arrays taken separately are strictly increasing.
        """

        # Create references
        if len(nums1) >= len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1

        total_length = len(long) + len(short)
        half = total_length // 2

        short_left, short_right = 0, len(short) - 1
        short_mid = (short_left + short_right) // 2

        while True:
            short_mid = (short_left + short_right) // 2

            a_idx = half - short_mid - 2
            a = -float('inf') if a_idx < 0 else long[a_idx]
            b = float('inf') if a_idx + 1 > len(long) - 1 else long[a_idx + 1]

            c = -float('inf') if short_mid < 0 else short[short_mid]
            d = float('inf') if short_mid + 1 > len(short) - 1 else short[short_mid + 1]

            if a <= d and c <= b:
                if total_length % 2 == 1:
                    return float(min(b, d))
                else:
                    return (max(a, c) + min(b, d)) / 2
            if not (c <= b):
                short_right = short_mid - 1
            else:
                short_left = short_mid + 1