class Solution:
    def toGoatLatin(self, S: str) -> str:

        words = S.split()
        results = []

        for i, word in enumerate(words):
            new_word = ""
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"

            new_word += 'a' * (i + 1)
            results.append(new_word)

        return " ".join(results)