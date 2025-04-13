class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        end = len(s) - 1
        start = 0

        temp = s
        while start <= end and s[start].isalnum() == False:
            start += 1
        
        while start <= end and s[end].isalnum() == False:
            end -= 1

        while start <= end:
            if temp[start].isalpha() and temp[end].isdigit():
                return False

            if temp[start].isdigit() and temp[end].isalpha():
                return False

            if temp[start].isdigit() and temp[start] != temp[end]:
                return False
            
            if temp[start].isalpha() and temp[start].lower() != temp[end].lower():
                return False
            
            start += 1
            end -= 1

            while start <= end and s[start].isalnum() == False:
                start += 1

            while start <= end and s[end].isalnum() == False:
                end -= 1

        return True
        """
        if s == "":
            return True
    
        left = 0
        right = len(s) - 1

        while left < right:
            while left < len(s) - 1 and not s[left].isalnum():
                left += 1
        
            while right >= 0 and not s[right].isalnum():
                right -= 1
        
            if left > right:
                return True

            if (s[left].isdigit() and not s[right].isdigit()) or (not s[left].isdigit() and s[right].isdigit()):
                return False
        
            if s[left].isdigit() and s[right].isdigit():
                if s[left] != s[right]:
                    return False
            else:
                if s[left].lower() != s[right].lower():
                    return False

            left += 1
            right -= 1
    
        return True