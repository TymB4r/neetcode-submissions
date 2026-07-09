from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def signature_string(string: str) -> tuple:
            presence_map = [0] * 26 # 26 because we only consider lowercase english letters
            for c in string:
                presence_map[ord(c) - ord('a')] += 1

            return tuple(presence_map)

        res = {}

        for string in strs:
            signature = signature_string(string)

            if signature in res:
                res[signature].append(string)
            else:
                res[signature] = [string]

        return list(res.values())