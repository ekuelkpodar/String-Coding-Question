class Solution:
    def maxPower(self, s: str) -> int:
        longest = 0

        count = 0
        prev = None

        for i, c in enumerate(s):
            if c == prev:
                count += 1
            else:
                longest = max(longest, count)
                prev = c
                count = 1

        return max(longest, count)