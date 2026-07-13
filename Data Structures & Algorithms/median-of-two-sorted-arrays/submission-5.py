from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        if not nums1 and not nums2:
            return 0
        if not nums1:
            return (nums2[(m - 1) // 2] + nums2[m // 2]) / 2
        if not nums2:
            return (nums1[(n - 1) // 2] + nums1[n // 2]) / 2

        # Create references
        if len(nums1) >= len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1

        long_target = (0 + len(long)) // 2 # Czy to zostawić tak czy lepiej zrobić len(long) // 2 po prostu?
        short_left, short_right = 0, len(short) - 1

        while short_right - short_left > 1:
            mid = (short_left + short_right) // 2

            if short[mid] == long[long_target]:
                return float(short[mid])
            elif short[mid] > long[long_target]:
                short_right = mid
                long_target += (mid - (short_right + short_left) // 2) # Difference between old and new mid
            else:
                short_left = mid
                long_target += (mid - (short_right + short_left) // 2)


        if (len(long) + len(short)) % 2 == 0:
            ele = max(long[long_target-1], short[short_left])
            return (long[long_target] + ele) / 2

        if long[long_target] < short[short_left]:
            return float(long[long_target])
        return float(short[short_left])
