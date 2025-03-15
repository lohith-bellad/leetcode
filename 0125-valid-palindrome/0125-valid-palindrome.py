class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []

        for c in s:
            if c.isalnum():
                if c.isalpha() and c.isupper():
                    temp.append(c.lower())
                else:
                    temp.append(c)
        
        end = len(temp) - 1
        start = 0

        while start <= end:
            if temp[start] != temp[end]:
                return False
            
            start += 1
            end -= 1
        
        return True