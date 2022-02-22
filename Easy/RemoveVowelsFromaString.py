class Solution:
    def removeVowels(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch not in ('a', 'e', 'i', 'o', 'u'):
                result += ch

        return result
