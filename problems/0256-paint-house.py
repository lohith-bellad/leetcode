"""
256. Paint House
Easy

There is a row of n houses, where each house can be painted one of three colors: red,
blue, or green. The cost of painting each house with a certain color is different.

You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost
matrix costs.
    * costs[i][0] is the cost of painting house i with the color red.
    * costs[i][1] is the cost of painting house i with the color blue.
    * costs[i][2] is the cost of painting house i with the color green.

Return the minimum cost to paint all houses.


Example 1:
    Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
    Output: 10
    Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
    into blue.
    Minimum cost: 2 + 5 + 3 = 10.

Example 2:
    Input: costs = [[7,6,2]]
    Output: 2


Constraints:
    * costs.length == n
    * costs[i].length == 3
    * 1 <= n <= 100
    * 1 <= costs[i][j] <= 20

"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}

        def dfs(house_ind, prev_color):
            if house_ind >= len(costs):
                return 0

            if (house_ind, prev_color) in memo:
                return memo[(house_ind, prev_color)]

            min_cost = float("inf")
            for color in range(3):
                if color == prev_color:
                    continue

                cost = costs[house_ind][color] + dfs(house_ind + 1, color)
                min_cost = min(min_cost, cost)

            memo[(house_ind, prev_color)] = min_cost
            return min_cost

        return dfs(0, -1)
