class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(unit, jump):
            if unit == stones[-1]:
                return True

            if unit not in stones_set:
                return False

            if (unit, jump) in cache:
                return cache[(unit, jump)]

            long_jump = dfs(unit + jump + 1, jump + 1)

            short_jump = False
            if jump != 1:
                short_jump = dfs(unit + jump - 1, jump - 1)
            
            med_jump = dfs(unit + jump, jump)

            cache[(unit, jump)] = long_jump or short_jump or med_jump
            return cache[(unit, jump)]
        
        cache = {}
        stones_set = set(stones)
        return dfs(stones[0] + 1, 1)
