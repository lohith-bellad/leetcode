class Solution:
    def isNumber(self, s: str) -> bool:
        is_number = False
        is_decimal = False
        is_exponent = False
    
        for i in range(len(s)):
            if s[i].isdigit():
                is_number = True
            elif s[i] in "+-":
                if i > 0 and s[i-1] != "e" and s[i-1] != "E":
                    return False
            elif s[i] == ".":
                if is_exponent or is_decimal:
                    return False
                is_decimal = True
            elif s[i] == "e" or s[i] == "E":
                if not is_number or is_exponent:
                    return False
                is_exponent = True
                is_number = False
            else:
                return False
        
        return is_number