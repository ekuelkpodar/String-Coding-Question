class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0

        mapping = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        for i in range(1, N + 1):

            i_str = str(i)

            rotated_str = ""
            can_rotate = True
            for c in i_str:
                if c not in mapping:
                    can_rotate = False
                    break
                rotated_str += mapping[c]

            if can_rotate and rotated_str != i_str:
                count += 1

        return count