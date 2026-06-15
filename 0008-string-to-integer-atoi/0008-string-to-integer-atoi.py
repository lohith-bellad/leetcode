class Solution:
    def myAtoi(self, s: str) -> int:
        """
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
        """
        is_neg = False
        ind = 0

        # trim starting white spaces
        while ind < len(s) and s[ind] == " ":
            ind += 1
            
        if ind < len(s) and s[ind] in "+-":
            if s[ind] == "-":
                is_neg = True
            ind += 1
        
        num = 0
        while ind < len(s) and s[ind].isdigit():
            num = (num * 10) + int(s[ind])
            ind += 1
        
        if is_neg:
            num = -num
        
        if num < -2**31:
            return -2**31
        
        if num > 2**31 - 1:
            return 2**31 - 1

        return num