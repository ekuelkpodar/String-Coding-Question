class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        words_dict = {}

        for i, word in enumerate(words):
            words_dict[i] = word

        for key, value in words_dict.items():
            if value.startswith(searchWord):
                return key + 1

        return -1
