class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        allowed = set(allowed)

        for word in words:
            i = 0

            while i < len(word):
                if word[i] not in allowed:
                    break
                i += 1

            if i == len(word):
                count += 1

        return count