class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_numerical = self.get_numerical(firstWord)
        second_numerical = self.get_numerical(secondWord)
        target_numerical = self.get_numerical(targetWord)

        return target_numerical == first_numerical + second_numerical

    def get_numerical(self, word):
        result = 0

        for c in word:
            result = 10 * result + (ord(c) - ord('a'))

        return result