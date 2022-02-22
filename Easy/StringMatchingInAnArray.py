class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        results = []

        words_set = set(words)

        for i, word in enumerate(words):
            for key in words_set:

                if key != word and key.find(word) != -1:
                    results.append(word)
                    break

        return results