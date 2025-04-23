class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
        row_max = len(grid)
        col_max = len(grid[0])
        
        queue = deque()
        second_queue = deque()
        first, second = -1, -1
        found = False
        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == 1:
                    found = True
                    queue.append((r, c))
                    second_queue.append((r, c, 0))
                    grid[r][c] = 2
                    break
            if found == True:
                break
        
        while len(queue) > 0:
            row, col = queue.popleft()
                    
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]
                        
                if 0 <= nrow < row_max and 0 <= ncol < col_max and grid[nrow][ncol] == 1:
                    queue.append((nrow, ncol))
                    second_queue.append((nrow, ncol, 0))
                    grid[nrow][ncol] = 2
                            
        while len(second_queue) > 0:
            row, col, dist = second_queue.popleft()

            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if 0 <= nrow < row_max and 0 <= ncol < col_max:
                    if grid[nrow][ncol] == 1:
                        return dist
                    elif grid[nrow][ncol] == 0:
                        grid[nrow][ncol] = -1
                        second_queue.append((nrow, ncol, dist + 1))