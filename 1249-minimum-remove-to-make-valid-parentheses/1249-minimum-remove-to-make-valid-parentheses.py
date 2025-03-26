class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bracket = []
        output = []
        temp = []

        for c in s:
            if c == ")":
                if len(bracket) > 0:
                    if bracket[-1] == "(":
                        bracket.pop()
                        output.append(c)
            elif c == "(":
                bracket.append(c)
                output.append(c)
            else:
                output.append(c)
        
        if len(bracket) == 0:
            return "".join(output)

        if len(bracket) > 0:
            bracket.pop()
            closed = 0
            while len(output) > 0:
                e = output.pop()
                if e == ")":
                    closed += 1
                    temp.append(e)
                elif e == "(":
                    if closed > 0:
                        closed -= 1
                        temp.append(e)
                else:
                    temp.append(e)
        
        temp.reverse()
        return "".join(temp)
        
    