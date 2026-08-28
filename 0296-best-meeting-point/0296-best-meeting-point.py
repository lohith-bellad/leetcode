class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def get_dist(nums):
            l = len(nums)
            output = float("inf")

            for i in range(l):
                temp = 0
                for j in range(l):
                    temp += abs(i - j) * nums[j]

                output = min(output, temp)

            return output

        hist_x = [0 for i in range(len(grid))]
        hist_y = [0 for i in range(len(grid[0]))]

        for i in range(len(grid)):
            hist_x[i] = sum(grid[i])
        
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                hist_y[c] += grid[r][c]

        hist_x_tot = get_dist(hist_x)
        hist_y_tot = get_dist(hist_y)

        return hist_x_tot + hist_y_tot
