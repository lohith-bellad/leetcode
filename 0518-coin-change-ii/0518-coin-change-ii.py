class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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