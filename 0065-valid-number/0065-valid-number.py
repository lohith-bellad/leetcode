class Solution:
    def isNumber(self, s: str) -> bool:
        """
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
        
        is_exp = False
        is_dot = False
        is_num = False
        is_sign = False

        for n in s:
            # check for signs:
            if n in "-+":
                if is_sign or (is_dot and not is_exp):
                    return False
                if is_num and not is_sign:
                    return False
                is_sign = True

            # Check for exponent
            elif n == 'e' or n == 'E':
                if is_exp or not is_num:
                    return False
                if is_sign:
                    is_sign = False
                is_exp = True
                is_num = False

            # check for decimal
            elif n == ".":
                if is_exp or is_dot:
                    return False
                is_dot = True

            # check for number
            elif n.isdigit():
                is_num = True

            # if anything else, bail-out
            else:
                return False

        return is_num
        """
        dot_found = False
        exp_found = False
        sign_found = False
        num_found = False

        for n in s:
            if n in "+-":
                if sign_found or (dot_found and not exp_found):
                    return False
                if num_found:
                    return False
                sign_found = True
            
            elif n == ".":
                if dot_found or exp_found:
                    return False
                dot_found = True

            elif n == "e" or n == "E":
                if exp_found or not num_found:
                    return False
                
                sign_found = False
                exp_found = True
                num_found = False

            elif n.isdigit():
                num_found = True
            
            else:
                return False
        
        return num_found