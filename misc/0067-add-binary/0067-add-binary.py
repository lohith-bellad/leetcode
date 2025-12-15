class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        result = ""

        while p1 >= 0 or p2 >= 0:
            n1 = 0
            n2 = 0
            if p1 >= 0:
                n1 = int(a[p1])
            if p2 >= 0:
                n2 = int(b[p2])

            if n1 == 1 and n2 == 1:
                if carry:
                    result += "1"
                else:
                    result += "0"
                carry = 1
            elif n1 ^ n2:
                if carry:
                    result += "0"
                else:
                    result += "1"
                    carry = 0
            else:
                if carry:
                    result += "1"
                    carry = 0
                else:
                    result += "0"
            p1 -= 1
            p2 -= 1

        if carry:
            result += "1"

        return result[::-1]
