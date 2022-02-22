class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        results = [None for i in range(len(words))]

        for word in words:
            i = int(word[-1])

            results[i - 1] = word[:len(word) - 1]

        return " ".join(results)
