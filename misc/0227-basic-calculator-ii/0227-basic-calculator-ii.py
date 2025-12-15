class Solution:
    def calculate(self, s: str) -> int:
        if s == "":
            return 0

        cal_stack = []
        s = s + "+"
        num = 0
        res = 0
        op = "+"

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+/*-":
                if op == "+":
                    cal_stack.append(num)
                elif op == "-":
                    cal_stack.append(-num)
                elif op == "*":
                    cal_stack.append(cal_stack.pop() * num)
                else:
                    cal_stack.append(int(cal_stack.pop() / num))
                num = 0
                op = c

        return sum(cal_stack)
