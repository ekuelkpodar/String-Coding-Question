class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        i = 0
        j = len(s)

        max_sub = ""

        for i in range(len(s)):
            for j in range(len(s), 0, -1):

                sub = s[i:j]

                lower_counter = set(sub.lower())
                upper_lower_counter = set(sub)

                if len(upper_lower_counter) == 2 * len(lower_counter):

                    if len(sub) > len(max_sub):
                        max_sub = sub

        return max_sub