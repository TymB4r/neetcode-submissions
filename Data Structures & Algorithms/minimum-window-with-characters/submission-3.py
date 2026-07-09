# Algorhythm is currently O(58N) but can be optimized to O(N),
# if we track the insufficiencies in counters instead of comparing them entirely at each step
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        def are_chars_in_range():
            for i in range(58):
                if s_counter[i] < t_counter[i]:
                    return False
            return True

        # There are 58 possible characters between A and z in ASCII. Indices from 26 to 31 will always remain empty.
        t_counter = [0] * 58
        s_counter = [0] * 58

        for c in t:
            t_counter[ord(c) - ord('A')] += 1

        left_idx, right_idx = 0, float('inf')
        left = 0
        for right in range(len(s)):
            s_counter[ord(s[right]) - ord('A')] += 1
            while are_chars_in_range():
                if right - left < right_idx - left_idx:
                    right_idx = right
                    left_idx = left

                s_counter[ord(s[left]) - ord('A')] -= 1
                left += 1

        if right_idx == float('inf'): # No substring of s containing characters from t was found
            return ""
        return s[left_idx:right_idx+1]