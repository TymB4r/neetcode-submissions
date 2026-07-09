from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        if nums.count(0) >= 2:
            return res

        if nums.count(0) == 1:
            zero_idx = nums.index(0)
            product_except_zero = 1
            for num in nums:
                if num != 0: product_except_zero *= num
            res[zero_idx] = product_except_zero
            return res

        # From here it's guaranteed, that no zeros will be present in nums
        curr_prefix_product = 1
        for i, num in enumerate(nums):
            res[i] = curr_prefix_product
            curr_prefix_product *= num

        print(res)
        curr_postfix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= curr_postfix_product
            curr_postfix_product *= nums[i]

        return res