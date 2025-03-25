class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 and j >= 0:
            if a[i] == "1" and b[j] == "1":
                if carry == 0:
                    result += '0'
                else:
                    result += '1'
                carry = 1
            elif (a[i] == "1" and b[j] == "0") or (a[i] == "0" and b[j] == "1"):
                if carry == 0:
                    result += '1'
                else:
                    result += '0'
            else:
                if carry == 0:
                    result += '0'
                else:
                    result += '1'
                    carry = 0
            i -= 1
            j -= 1
        
        if len(a) > len(b):
            print(i)
            while i >= 0:
                if a[i] == "1":
                    if carry == 0:
                        result += '1'
                    else:
                        result += '0'
                else:
                    if carry == 0:
                        result += '0'
                    else:
                        result += '1'
                        carry = 0
                i -= 1
        
        if len(a) < len(b):
            while j >= 0:
                if b[j] == "1":
                    if carry == 0:
                        result += '1'
                    else:
                        result += '0'
                else:
                    if carry == 0:
                        result += '0'
                    else:
                        result += '1'
                        carry = 0
                j -= 1
       
        if carry == 1:
            result += '1'

        return result[::-1]        