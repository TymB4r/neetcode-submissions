from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def characterize_string(string: str) -> str:
            presence_map = [0] * 26
            for key, value in Counter(string).items():
                presence_map[ord(key) - ord('a')] += value

            characterized = ','.join(str(value) for value in presence_map)
            return characterized

        res = []
        characterized_to_output_idx = {}

        for idx, string in enumerate(strs):
            characterized = characterize_string(string)
            if characterized in characterized_to_output_idx:
                res_idx = characterized_to_output_idx[characterized]
                res[res_idx].append(string)
            else:
                res.append([string])
                characterized_to_output_idx[characterized] = len(characterized_to_output_idx)

        return res