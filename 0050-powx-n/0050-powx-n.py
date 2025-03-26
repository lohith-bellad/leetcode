class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
            n *= -1
        result = 1.0
        while n > 0:
            if (n % 2 == 1):
                result *= x
            n = n // 2
            x = x * x
        
        return result