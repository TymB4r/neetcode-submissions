class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        cur_set = set()

        left = 0
        for right in range(len(s)):
            while s[right] in cur_set:
                cur_set.remove(s[left])
                left += 1

            max_length = max(max_length, right - left + 1)
            cur_set.add(s[right])

        return max_length