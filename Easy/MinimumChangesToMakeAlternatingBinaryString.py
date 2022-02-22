class Solution:
    def minOperations(self, s: str) -> int:

        s_arr = list(s)

        zero_start_arr = ['0' if i % 2 else '1' for i in range(len(s))]
        one_start_arr = ['1' if i % 2 else '0' for i in range(len(s))]

        min_count = sys.maxsize

        zero_start_count = 0
        for c, z_c in zip(s_arr, zero_start_arr):
            if c != z_c:
                zero_start_count += 1

        one_start_count = 0
        for c, o_c in zip(s_arr, one_start_arr):
            if c != o_c:
                one_start_count += 1

        return min(one_start_count, zero_start_count)