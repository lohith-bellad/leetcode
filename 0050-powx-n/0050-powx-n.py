class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1.0 / x
            n = -n
        
        res = 1.0
        while n > 0:
            if n % 2 == 1:
                res *= x
                n -= 1

            x = x * x
            n = n // 2
        
        return res