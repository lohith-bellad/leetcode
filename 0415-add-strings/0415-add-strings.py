class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_list = list(num1)
        num2_list = list(num2)
        output = []
        carry = 0

        while num1_list and num2_list:
            a = int(num1_list.pop())
            b = int(num2_list.pop())
            total = a + b + carry
            carry = total // 10
            total = total % 10
            

            output.append(str(total))
        
        while num1_list:
            total = int(num1_list.pop()) + carry
            carry = total // 10
            total = total % 10
            output.append(str(total))
        
        while num2_list:
            total = int(num2_list.pop()) + carry
            carry = total // 10
            total = total % 10
            output.append(str(total))

        if carry > 0:
            output.append(str(carry))
        
        output.reverse()
        return "".join(output)