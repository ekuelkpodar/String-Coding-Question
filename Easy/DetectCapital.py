class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        upper_count = 0
        for c in word:

            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                upper_count += 1

        if upper_count == 0:
            return True

        if upper_count == len(word):
            return True

        if upper_count == 1 and ord(word[0]) >= ord('A') and ord(word[0]) <= ord('Z'):
            return True

        return False