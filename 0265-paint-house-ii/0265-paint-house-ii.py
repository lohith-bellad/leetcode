class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
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
        """
        def dfs(h_ind, c_ind):
            if h_ind == max_houses:
                return 0

            if (h_ind, c_ind) in cache:
                return cache[(h_ind, c_ind)]

            r = float('inf')
            for c in range(max_colors):
                if c == c_ind:
                    continue
                r = min(r, dfs(h_ind + 1, c) + costs[h_ind][c_ind])

            cache[(h_ind, c_ind)] = r
            return r
        
        max_houses = len(costs)
        max_colors = len(costs[0])

        cache = {}
        res = float('inf')
        for c in range(max_colors):
            res = min(res, dfs(0, c))

        return res