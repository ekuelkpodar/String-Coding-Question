class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        counter = {}

        for c in text:
            counter[c] = counter.get(c, 0) + 1

        count = 0

        stop = False
        while not stop:

            is_finish = True
            for c in "balloon":
                counter[c] = counter.get(c, 0) - 1

                if counter[c] < 0:
                    stop = True
                    is_finish = False
                    break

            if is_finish:
                count += 1

        return count
