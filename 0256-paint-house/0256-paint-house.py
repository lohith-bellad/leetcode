class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        def dfs(house_ind, prev_color):
            if house_ind >= len(costs):
                return 0

            if (house_ind, prev_color) in cache:
                return cache[(house_ind, prev_color)]

            min_cost = float("inf")
            for color in range(3):
                if color == prev_color:
                    continue

                cur_cost = costs[house_ind][color] + dfs(house_ind + 1, color)
                min_cost = min(min_cost, cur_cost)

            cache[(house_ind, prev_color)] = min_cost
            return min_cost

        cache = {}
        v = dfs(0, -1)
        print(cache)
        return v
        """
        def dfs(house, color):
            if house == len(costs):
                return 0

            if (house, color) in cache:
                return cache[(house, color)]

            res = float('inf')
            for c in range(3):
                if c == color:
                    continue
                res = min(res, dfs(house + 1, c) + costs[house][color])

            cache[(house, color)] = res
            return res

        output = float('inf')
        cache = {}
        for color in range(3):
            output = min(output, dfs(0, color))

        return output