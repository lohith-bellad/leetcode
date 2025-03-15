class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        temp = []

        for c in s:
            if c.isalnum():
                if c.isalpha() and c.isupper():
                    temp.append(c.lower())
                else:
                    temp.append(c)
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