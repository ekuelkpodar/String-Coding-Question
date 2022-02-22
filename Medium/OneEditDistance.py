class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False

        if abs(len(s) - len(t)) > 1:
            return False

        if abs(len(s) - len(t)) == 0:
            diff_count = 0

            for c1, c2 in zip(s, t):
                if c1 != c2:
                    diff_count += 1

            if diff_count > 1:
                return False
            else:
                return True
        else:
            long = s if len(s) > len(t) else t
            short = t if len(s) > len(t) else s

            for i in range(len(long)):
                after_delete = long[:i] + long[i + 1:]

                if after_delete == short:
                    return True

            return False
