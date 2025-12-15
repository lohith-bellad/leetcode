class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        res = []
        carry = 0

        while p1 >= 0 or p2 >= 0:
            n1 = 0
            n2 = 0
            if p1 >= 0:
                n1 = int(num1[p1])
            if p2 >= 0:
                n2 = int(num2[p2])

            total = n1 + n2 + carry
            carry = total // 10
            total = total % 10

            res.append(str(total))
            p1 -= 1
            p2 -= 1

        if carry > 0:
            res.append(str(carry))

        res.reverse()
        return "".join(res)
