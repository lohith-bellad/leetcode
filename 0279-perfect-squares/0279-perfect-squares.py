class Solution:
    def numSquares(self, n: int) -> int:
        """
        def traverse(num: int) -> int:
            if num == 0:
                return 0
            
            if num < 0:
                return float('inf')

            if num in cache:
                return cache[num]

            iter = 1
            res = float('inf')
            while iter**2 <= num:
                res = min(res, traverse(num - iter**2))
                iter += 1
            
            cache[num] = res + 1
            return cache[num]
        
        cache = {}
        return traverse(n)
        """
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0

        for s in range(n + 1):
            iter = 1
            while iter**2 <= s:
                dp[s] = min(dp[s], dp[s - iter**2] + 1)
                iter += 1
        
        return dp[n]
