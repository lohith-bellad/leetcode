class Solution:
    def climbStairs(self, n: int) -> int:
        """
        memo = {}
        def climb(step: int, memo):
            if step <= 2:
                return step
            
            if step in memo:
                return memo[step]

            memo[step] = climb(step - 1, memo) + climb(step - 2, memo)
            return memo[step]
        
        return climb(n, memo)
        """
        def traverse(steps):
            if steps <= 2:
                return steps

            if steps not in cache:
                cache[steps] =  traverse(steps - 1) + traverse(steps - 2)

            return cache[steps]
        
        cache = {}
        return traverse(n)