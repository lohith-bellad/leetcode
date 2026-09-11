class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(unit, jump):
            if unit == stones[-1]:
                return True

            if unit not in stones_set:
                return False

            if (unit, jump) in cache:
                return cache[(unit, jump)]

            result = (dfs(unit + jump + 1, jump + 1) or
                    dfs(unit + jump, jump) or
                    (jump > 1 and dfs(unit + jump - 1, jump - 1)))

            cache[(unit, jump)] = result
            return cache[(unit, jump)]
        
        cache = {}
        stones_set = set(stones)
        return dfs(stones[0] + 1, 1)
