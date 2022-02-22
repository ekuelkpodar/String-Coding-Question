class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        lines_counter = {}

        line_width = 0
        line_count = 0

        for c in s:
            w = widths[ord(c) - ord('a')]

            if line_width + w <= 100:
                line_width = line_width + w
                lines_counter[line_count] = line_width
            else:
                line_count += 1
                lines_counter[line_count] = w
                line_width = w

        return [line_count + 1, lines_counter[line_count]]
