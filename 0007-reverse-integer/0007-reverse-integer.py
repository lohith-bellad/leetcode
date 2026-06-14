class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False

        if x < 0:
            is_neg = True
            x = -x

        num = 0
        while x > 0:
            num = (num * 10) + (x % 10)
            x = x // 10
        
        if (num > 2**31 - 1) or (is_neg and num > 2**31):
            return 0
        
        if is_neg:
            return -num
        
        return num