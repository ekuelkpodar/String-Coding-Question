class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        count = 0

        for i in range(len(s) - k + 1):
            visited = set()

            for j in range(i, i + k):

                c = s[j]

                if c in visited:
                    break
                else:
                    visited.add(c)

            if len(visited) == k:
                count += 1

        return count