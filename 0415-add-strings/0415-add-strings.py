class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        output = ""

        while p1 >= 0 or p2 >= 0:
            n1 = n2 = 0
            if p1 >= 0:
                n1 = int(num1[p1])
            if p2 >= 0:
                n2 = int(num2[p2])
            
            s = n1 + n2 + carry
            carry = s // 10
            output += str(s % 10)

            p1 -= 1
            p2 -= 1
        
        if carry:
            output += str(carry)
        
        return output[::-1]