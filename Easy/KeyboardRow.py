class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        results = []

        row1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        row2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        row3 = ["z", "x", "c", "v", "b", "n", "m"]

        for word in words:
            is_same = True
            prev_row = 0

            for c in word.lower():
                row = None

                if c in row1:
                    row = 1
                elif c in row2:
                    row = 2
                elif c in row3:
                    row = 3

                if prev_row != 0 and row != prev_row:
                    is_same = False
                    break

                prev_row = row

            if is_same:
                results.append(word)

        return results
