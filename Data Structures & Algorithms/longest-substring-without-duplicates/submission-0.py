from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_to_count = defaultdict(int)

        l, r = 0, 0

        while r < len(s):
            right_char = s[r]
            char_to_count[right_char] += 1

            while char_to_count[right_char] > 1:
                left_char = s[l]
                char_to_count[left_char] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length