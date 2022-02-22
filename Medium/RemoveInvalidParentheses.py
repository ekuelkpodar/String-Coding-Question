class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        results = []

        left, right = self.left_right_count(s)

        self.dfs_helper(s, left, right, 0, results)

        return results

    def left_right_count(self, s):
        left = 0
        right = 0

        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        return left, right

    def is_valid(self, s):
        left, right = self.left_right_count(s)
        return left == 0 and right == 0

    def dfs_helper(self, s, left, right, start, results):
        if left == 0 and right == 0:
            if self.is_valid(s):
                results.append(s)
                return

        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue

            if s[i] == '(':
                self.dfs_helper(s[:i] + s[i + 1:], left - 1, right, i, results)
            elif s[i] == ')':
                self.dfs_helper(s[:i] + s[i + 1:], left, right - 1, i, results)