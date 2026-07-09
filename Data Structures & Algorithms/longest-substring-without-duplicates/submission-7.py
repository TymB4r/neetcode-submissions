class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        last_seen = {}

        left = 0
        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1

            max_length = max(max_length, right - left + 1)
            last_seen[c] = right

        return max_length