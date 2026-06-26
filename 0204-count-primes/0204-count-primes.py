class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for i in range(n)]
        primes[0:2] = [False, False]

        for c in range(2, int(n**0.5) + 1):
            if primes[c]:
                for i in range(c * c, n, c):
                    primes[i] = False
        
        output = 0
        for i in range(n):
            if primes[i]:
                output += 1
        
        return output