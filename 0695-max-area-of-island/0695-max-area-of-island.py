class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(grid)
        col_max = len(grid[0])
        queue = deque()
        max_area = float("-inf")

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == 1:
                    cur_area = 1
                    grid[r][c] = 0
                    queue.append((r, c))

                    while queue:
                        row, col = queue.popleft()

                        for d in dir:
                            nrow = row + d[0]
                            ncol = col + d[1]

                            if (0 <= nrow < row_max and
                                0 <= ncol < col_max and
                                grid[nrow][ncol] == 1):
                                cur_area += 1
                                grid[nrow][ncol] = 0
                                queue.append((nrow, ncol))
                    
                    max_area = max(max_area, cur_area)
        
        if max_area == float("-inf"):
            return 0
        
        return max_area
