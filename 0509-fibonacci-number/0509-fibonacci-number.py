class Solution:
    def fib(self, n: int) -> int:
        """
        def traverse(n: int, cache: []) -> int:
            if n <= 1:
                return n
            
            if cache[n] != -1:
                return cache[n]
            
            cache[n] = traverse(n-1, cache) + traverse(n-2, cache)

            return cache[n]
        
        cache = [-1 for i in range(n + 1)]
        return traverse(n, cache)

        """
        def dp(num):
            if num < 2:
                return num

            if num not in cache:
                cache[num] = dp(num - 1) + dp(num - 2)

            return cache[num]

        cache = {}
        return dp(n)