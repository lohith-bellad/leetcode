class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_list = list(num1)
        num2_list = list(num2)
        output = []
        carry = 0

        while num1_list or num2_list:
            if num1_list:
                a = int(num1_list.pop())
            else:
                a = 0
            
            if num2_list:
                b = int(num2_list.pop())
            else:
                b = 0

            total = a + b + carry
            carry = total // 10
            total = total % 10
            output.append(str(total))
        
        if carry > 0:
            output.append(str(carry))
        
        output.reverse()
        return "".join(output)