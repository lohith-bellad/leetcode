class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        is_neg = False

        idx = 0
        while idx < len(s) and s[idx] == " ":
            idx += 1

        if idx < len(s) and s[idx] in "+-":
            if s[idx] == "-":
                is_neg = True
            idx += 1

        while idx < len(s):
            if s[idx].isdigit():
                n = int(s[idx])
                num = (num * 10) + n
                idx += 1
            elif num == 0:
                return 0
            else:
                break
            
        
        if is_neg:
            num = -num

        if num < (2**31)*(-1):
            return (2**31)*-1

        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num