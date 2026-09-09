class Solution:
    def minDays(self, n: int) -> int:
        """
        def dfs(rem_oranges):
            if rem_oranges == 0:
                return rem_oranges
            
            if rem_oranges in cache:
                return cache[rem_oranges]

            eat_single = dfs(rem_oranges - 1)

            eat_half = float('inf')
            if rem_oranges % 2 == 0:
                eaten = rem_oranges / 2
                eat_half = dfs(rem_oranges - eaten)
            
            eat_two_third = float('inf')
            if rem_oranges % 3 == 0:
                eaten = 2 * rem_oranges / 3
                eat_two_third = dfs(rem_oranges - eaten)
            
            cache[rem_oranges] = min(eat_single, eat_half, eat_two_third) + 1
            return cache[rem_oranges]

        cache = {}
        return dfs(n)
        """
        
        def dfs(rem_oranges):
            if rem_oranges <= 1:
                return rem_oranges

            if rem_oranges in cache:
                return cache[rem_oranges]

            # eat rem % 2 singles to reach a multiple of 2, then halve
            eat_half = rem_oranges % 2 + dfs(rem_oranges // 2)
            # eat rem % 3 singles to reach a multiple of 3, then eat two-thirds
            eat_two_third = rem_oranges % 3 + dfs(rem_oranges // 3)

            cache[rem_oranges] = min(eat_half, eat_two_third) + 1
            return cache[rem_oranges]

        cache = {}
        return dfs(n)