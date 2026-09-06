class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        row_max = len(costs)
        col_max = len(costs[0])

        def dfs(house, color):
            if house >= row_max:
                return 0
            
            if (house, color) in cache:
                return cache[(house, color)]

            cost = float('inf')
            for c in range(col_max):
                if c == color:
                    continue
                
                cost = min(cost, dfs(house + 1, c) + costs[house][color])
            
            cache[(house, color)] = cost
            return cost

        cache = {}
        r = float('inf')
        for col in range(col_max):
            r = min(r, dfs(0, col))
        
        return r
