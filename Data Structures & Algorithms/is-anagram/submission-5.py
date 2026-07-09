from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_frequency = defaultdict(int)
        t_letter_frequency = defaultdict(int)

        for letter in s:
            s_letter_frequency[letter] += 1

        for letter in t:
            t_letter_frequency[letter] += 1

        return s_letter_frequency == t_letter_frequency