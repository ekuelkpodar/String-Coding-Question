class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        results = []

        for i in range(0, len(currentState) - 1):
            sub = currentState[i:i+2]

            if sub == "++":
                flip = currentState[:i] + "--" + currentState[i+2:]
                results.append(flip)


        return results