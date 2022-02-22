class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_ones = 0
        longest_zeros = 0

        ones = 0
        zeros = 0

        for c in s:
            if c == '1':
                ones += 1
                longest_zeros = max(longest_zeros, zeros)
                zeros = 0
            else:
                zeros += 1
                longest_ones = max(longest_ones, ones)
                ones = 0

        longest_zeros = max(longest_zeros, zeros)
        longest_ones = max(longest_ones, ones)

        return longest_ones > longest_zeros