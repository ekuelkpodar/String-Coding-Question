class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""

        for i, c in enumerate(s):
            if i % 2 == 0:
                result += c
            else:
                result += chr(ord(s[i - 1]) + int(c))

        return result