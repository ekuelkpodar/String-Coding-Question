class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        result = 0
        counter = {}
        j = 0

        for i in range(len(s)):
            while j < len(s) and (len(counter) < k or (len(counter) == k and s[j] in counter)):
                counter[s[j]] = counter.get(s[j], 0) + 1

                j += 1

            if len(counter) <= k:
                result = max(result, j - i)

            counter[s[i]] -= 1

            if counter[s[i]] == 0:
                del counter[s[i]]

        return result