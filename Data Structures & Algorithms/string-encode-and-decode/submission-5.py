from typing import List


class Solution:
    def __init__(self):
        self.gaps = []

    def encode(self, strs: List[str]) -> str:
        self.gaps.append(0)
        cur_gap_idx = 0
        
        for string in strs:
            cur_gap_idx += len(string)
            self.gaps.append(cur_gap_idx)

        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(self.gaps) - 1):
            start_idx = self.gaps[i]
            end_idx = self.gaps[i + 1]
            res.append(s[start_idx:end_idx])
            
        return res