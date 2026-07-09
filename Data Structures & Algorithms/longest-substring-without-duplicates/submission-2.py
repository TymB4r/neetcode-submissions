class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        cur_set = set()

        l, r = 0, 0

        while r < len(s):
            while s[r] in cur_set:
                cur_set.remove(s[l])
                l += 1

            max_length = max(max_length, r - l + 1)
            cur_set.add(s[r])
            r += 1

        return max_length