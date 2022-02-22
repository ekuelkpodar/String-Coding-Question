class Solution:
    def generateTheString(self, n: int) -> str:
        if n < 2:
            return 'a'

        if n % 2 == 0:

            return 'a' * (n - 1) + 'b' * 1
        else:
            return 'a' * n

        return ""
