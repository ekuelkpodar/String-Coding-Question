class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        results = []

        text = text.split()

        i = 0

        while i < len(text) - 2:

            if text[i] == first and text[i + 1] == second:
                results.append(text[i + 2])

            i += 1

        return results
