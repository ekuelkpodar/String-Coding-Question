class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count_s1 = {}

        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1

        count_s2 = {}
        for c in s2:
            count_s2[c] = count_s2.get(c, 0) + 1

        for key, value in count_s1.items():
            if key not in count_s2 or value != count_s2[key]:
                return False

        count_mismatch = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count_mismatch += 1

        if count_mismatch > 2:
            return False

        return True