class Solution:
    def maxScore(self, s: str) -> int:
        split = 1

        max_score = 0
        while split < len(s):
            left = s[:split]
            right = s[split:]

            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)

            split += 1

        return max_score