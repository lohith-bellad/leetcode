class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev_num = 0
        num = x

        while num > 0:
            rev_num = (rev_num * 10) + (num % 10)
            num = num // 10
        
        return rev_num == x