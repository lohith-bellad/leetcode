class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
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