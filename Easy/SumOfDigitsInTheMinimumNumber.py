class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_num = min(A)

        digit_sum = 0
        for c in str(min_num):
            digit_sum += int(c)

        return 1 if digit_sum % 2 == 0 else 0