class Solution:
    def minDays(self, n: int) -> int:
        def dfs(rem_oranges):
            if rem_oranges <= 1:
                return rem_oranges
            
            if rem_oranges in cache:
                return cache[rem_oranges]

            eat_half = rem_oranges % 2 + dfs(rem_oranges // 2)
            eat_two_third = rem_oranges % 3 + dfs(rem_oranges // 3)
            
            cache[rem_oranges] = min(eat_half, eat_two_third) + 1
            return cache[rem_oranges]

        cache = {}
        return dfs(n)