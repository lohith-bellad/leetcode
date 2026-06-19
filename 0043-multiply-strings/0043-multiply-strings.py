class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        def get_product(num: str, digit: str) -> str:
            output = ""
            carry = 0

            d = int(digit)
            ind = len(num) - 1

            while ind >= 0:
                n = int(num[ind])
                prod = n * d + carry
                carry = prod // 10
                p = prod % 10

                output += str(p)
                ind -= 1
            
            if carry > 0:
                output += str(carry)
            
            return output[::-1]
        
        if num1 == "0" or num2 == "0":
            return "0"
        prods = []
        l = 0
        for i in range(len(num1) - 1, -1, -1):
            t = get_product(num2, num1[i]) + "0" * (len(num1) - i - 1)
            prods.append(t[::-1])
            l = max(l, len(t))
    
        result = ""
        carry = 0
        for i in range(l):
            cur_sum = 0
            for prod in prods:
                if i < len(prod):
                    cur_sum += int(prod[i])

            cur_sum += carry
            result += str(cur_sum % 10)
            carry = cur_sum // 10

        if carry > 0:
            result += str(carry)

        return result[::-1]
        """
        def addStrings(num1: str, num2: str) -> str:
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
    
        if not int(num1) or not int(num2):
            return str(0)
             
        if len(num1) > len(num2):
            num1, num2 = num1, num2

        hashMap = {}
        n2 = int(num2)
        num1 = num1[::-1]

        for i in range(len(num1)):
            res = int(num1[i]) * n2
            hashMap[i] = str(res) + '0' * i
        
        output = "0"

        for i in range(len(num1)):
            output = addStrings(output, hashMap[i])
        
        return output