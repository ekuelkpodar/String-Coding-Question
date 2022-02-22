class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1

        S_list = list(S)

        while i < j:
            if S_list[i].isalpha() and S_list[j].isalpha():
                temp = S_list[j]
                S_list[j] = S_list[i]
                S_list[i] = temp

                i += 1
                j -= 1
            elif S_list[i].isalpha():
                j -= 1
            elif S_list[j].isalpha():
                i += 1
            else:
                i += 1
                j -= 1

        return "".join(S_list)