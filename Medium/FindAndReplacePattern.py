class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        pattern_group = defaultdict(list)

        for i, c in enumerate(pattern):
            pattern_group[c].append(i)

        results = []

        for word in words:
            group = defaultdict(list)

            for i, c in enumerate(word):
                group[c].append(i)

            if list(group.values()) == list(pattern_group.values()):
                results.append(word)

        return results