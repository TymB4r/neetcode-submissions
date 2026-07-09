from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def characterize_string(string: str) -> tuple:
            presence_map = [0] * 26 # 26 because we only consider lowercase english letters
            for c in string:
                presence_map[ord(c) - ord('a')] += 1

            return tuple(presence_map)

        res = []
        characterized_to_output_idx = {}

        for string in strs:
            characterized = characterize_string(string)

            if characterized in characterized_to_output_idx:
                res_idx = characterized_to_output_idx[characterized]
                res[res_idx].append(string)
            else:
                # Number of keys in characterized_to_output_idx -> number of existing groups in res,
                # Next group's index -> len(characterized_to_output_idx) - 1 + 1
                characterized_to_output_idx[characterized] = len(characterized_to_output_idx)
                res.append([string])

        return res