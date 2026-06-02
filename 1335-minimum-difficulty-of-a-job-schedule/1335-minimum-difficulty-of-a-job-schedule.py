class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def dp(ind, days):
            if days == 1:
                cache[(ind, days)] = max(jobDifficulty[ind:])
                return cache[(ind, days)]

            if (ind, days) in cache:
                return cache[(ind, days)]
                
            day_max = 0
            best = float("inf")

            for i in range(ind, len(jobDifficulty) - days + 1):
                day_max = max(day_max, jobDifficulty[i])
                best = min(best, day_max + dp(i + 1, days - 1))
            
            cache[(ind, days)] = best
            return cache[(ind, days)]

        if len(jobDifficulty) < d:
            return -1
        
        cache = {}
        return dp(0, d)