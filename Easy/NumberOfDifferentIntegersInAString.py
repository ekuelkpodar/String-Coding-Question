class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        digit_str = ""
        for c in word:
            if not c.isdigit():
                digit_str += " "
            else:
                digit_str += c

        numbers = digit_str.split()

        numbers_set = set()

        for number in numbers:
            numbers_set.add(int(number))

        return len(numbers_set)