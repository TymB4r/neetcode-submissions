from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_to_count = defaultdict(int)
        max_width, max_count = 0, 0

        l = 0
        for r, c in enumerate(s):
            char_to_count[c] += 1
            max_count = max(max_count, char_to_count[c])

            while r - l + 1 - max_count > k:
                char_to_count[s[l]] -= 1
                l += 1

            max_width = max(max_width, r - l + 1)

        return max_width