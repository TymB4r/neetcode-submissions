from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The space complexity remains O(1), due to the maps having at most 26 entries
        if len(s) != len(t):
            return False
        
        if Counter(s) == Counter(t):
            return True
        return False