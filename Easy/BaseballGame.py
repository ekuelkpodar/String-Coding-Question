class Solution:
    def calPoints(self, ops: List[str]) -> int:
        results = []

        for op in ops:
            if op.isdigit() or op.startswith('-'):
                results.append(int(op))
            elif op == 'C':
                results.pop()
            elif op == 'D':
                results.append(results[-1] * 2)
            elif op == '+':
                results.append(results[-1] + results[-2])

        return sum(results)