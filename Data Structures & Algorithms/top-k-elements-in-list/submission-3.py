from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        freq_to_num = defaultdict(set)

        for num in nums:
            if num_to_freq[num] != 0: # If num == 0, it's not present in any freq_to_num subgroup
                freq_to_num[num_to_freq[num]].remove(num)
            num_to_freq[num] += 1
            freq_to_num[num_to_freq[num]].add(num)

        res = []
        cur_idx = len(freq_to_num) # len(freq_to_num) == maximum frequency of any number in nums
        while len(res) < k:
            cur_group = freq_to_num[cur_idx]
            for num in cur_group:
                res.append(num)
                if len(res) == k:
                    break
            cur_idx -= 1

        return res