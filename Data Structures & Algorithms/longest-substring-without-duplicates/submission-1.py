from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_to_count = defaultdict(int)

        l, r = 0, 0

        while r < len(s):
            char_to_count[s[r]] += 1

            while char_to_count[s[r]] > 1:
                char_to_count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length