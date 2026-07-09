from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = Counter(s1)
        s2_count = defaultdict(int)

        for i in range(n1):
            s2_count[s2[i]] += 1

        for i in range(n1, n2):
            if s1_count == s2_count:
                return True
            
            s2_count[s2[i-n1]] -= 1
            if s2_count[s2[i-n1]] == 0:
                del s2_count[s2[i-n1]]
                
            s2_count[s2[i]] += 1

        return s1_count == s2_count