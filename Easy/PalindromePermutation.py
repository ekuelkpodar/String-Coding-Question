class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = {}

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        number_of_odds = 0
        number_of_evens = 0

        for key, value in counter.items():
            if value % 2 == 0:
                number_of_evens += 1
            else:
                number_of_odds += 1

        if number_of_odds > 1:
            return False

        return True