class Solution:
    def calculate(self, s: str) -> int:
        cstack = []
        idx = 0

        while idx < len(s):
            if s[idx] == " ":
                idx += 1
                continue
            if s[idx].isdigit():
                num2 = 0
                while idx < len(s) and s[idx].isdigit():
                    num2 = (num2 * 10) + int(s[idx])
                    idx += 1
                idx -= 1
                if len(cstack) > 0 and (cstack[-1] == "*" or cstack[-1] == "/"):
                    op = cstack.pop()
                    num1 = cstack.pop()
                    if op == "*":
                        cstack.append(num1 * num2)
                    else:
                        cstack.append(num1 // num2)
                else:
                    cstack.append(num2)
            else:
                cstack.append(s[idx])
            idx += 1

        cstack.reverse()
        print(cstack)
        while len(cstack) > 1:
            num1 = cstack.pop()
            op = cstack.pop()
            num2 = cstack.pop()
            if op == "+":
                cstack.append(num1 + num2)
            else:
                cstack.append(num1 - num2)

        return cstack.pop()
