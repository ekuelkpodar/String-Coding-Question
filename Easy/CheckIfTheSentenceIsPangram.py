class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = {}

        for i in range(26):
            counter[chr(ord('a') + i)] = 0

        for c in sentence:
            counter[c] = counter.get(c, 0) + 1

        for key, value in counter.items():
            if value < 1:
                return False

        return True