class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        need = [0] * 26
        window = [0] * 26

        for i in range(n1):
            need[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1

        if window == need:
            return True

        for i in range(n1, n2):
            window[ord(s2[i]) - 97] += 1
            window[ord(s2[i - n1]) - 97] -= 1

            if window == need:
                return True

        return False