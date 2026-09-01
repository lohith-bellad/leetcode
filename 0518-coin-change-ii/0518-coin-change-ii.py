class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        def dfs(ind, cur_sum):
            if cur_sum == amount:
                return 1

            if ind >= len(coins) or cur_sum > amount:
                return 0

            if (ind, cur_sum) in cache:
                return cache[(ind, cur_sum)]

            cur_sum += coins[ind]
            opt1 = dfs(ind, cur_sum)
            cur_sum -= coins[ind]
            opt2 = dfs(ind + 1, cur_sum)

            cache[(ind, cur_sum)] = opt1 + opt2
            return cache[(ind, cur_sum)]

        cache = {}
        return dfs(0, 0)
        """
        n = len(coins)

        dp = [[0 for i in range(amount + 1)] for i in range(n+1)]

        for i in range(n + 1):
            dp[i][amount] = 1
        
        for ind in range(n - 1, -1, -1):
            for s in range(amount -1, -1, -1):
                take = dp[ind][s + coins[ind]] if s + coins[ind] <= amount else 0
                skip = dp[ind + 1][s]
                dp[ind][s] = take + skip
        
        return dp[0][0]
                