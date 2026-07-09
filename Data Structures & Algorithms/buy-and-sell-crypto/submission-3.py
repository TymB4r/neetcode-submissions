from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        max_difference = 0

        for price in prices[1:]:
            max_difference = max(max_difference, price - min_left)
            min_left = min(min_left, price)

        return max_difference