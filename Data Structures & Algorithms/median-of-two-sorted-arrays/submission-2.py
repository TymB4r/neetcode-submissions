from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return None
        if not nums1:
            return (nums2[(len(nums2) - 1) // 2] + nums2[(len(nums2)) // 2]) / 2
        if not nums2:
            return (nums1[(len(nums1) - 1) // 2] + nums1[(len(nums1)) // 2]) / 2

        if len(nums1) >= len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1

        long_target = (0 + len(long)) // 2

        short_left, short_right = 0, len(short) - 1

        while short_right - short_left > 1:
            mid = (short_left + short_right) // 2

            if short[mid] == long[long_target]:
                return short[mid]
            elif short[mid] > long[long_target]:
                short_right = mid
                long_target += (mid - (short_right + short_left) // 2) # Difference between mids
            else:
                short_left = mid
                long_target += (mid - (short_right + short_left) // 2)


        if (len(long) + len(short)) % 2 == 0:
            a = max(long[long_target-1], short[short_left])
            return (long[long_target] + a) / 2

        if long[long_target] < short[short_left]:
            return long[long_target]
        else:
            return short[short_left]