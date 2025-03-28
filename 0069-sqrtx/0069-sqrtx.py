class Solution:
    def mySqrt(self, x: int) -> int:
        guess = 1

        while (guess * guess) <= x:
            guess += 1
        
        return guess - 1