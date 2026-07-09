from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def characterize_string(string: str) -> tuple:
            presence_map = [0] * 26 # 26 because we only consider lowercase english letters
            for c in string:
                presence_map[ord(c) - ord('a')] += 1

            return tuple(presence_map)

        res = {}

        for string in strs:
            characterized = characterize_string(string)

            if characterized in res:
                res[characterized].append(string)
            else:
                res[characterized] = [string]

        return list(res.values())