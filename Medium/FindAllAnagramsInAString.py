class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []

        p_set = collections.Counter(p)
        len_p = len(p)

        for i in range(len(s) - len_p + 1):
            sub = s[i: i + len_p]

            if collections.Counter(sub) == p_set:
                results.append(i)

        return results