class Solution:
    def countLetters(self, S: str) -> int:

        count = 0

        for i in range(len(S)):
            for j in range(i + 1, len(S) + 1):

                sub = S[i:j]
                sub_set = set(sub)

                if len(sub_set) == 1:
                    count += 1
                else:
                    break

        return count