class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        butti = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
        queue = deque()
        row = [0, 0, -1, 1]
        col = [1, -1, 0, 0]
        row_max = len(grid)
        col_max = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    butti[i][j] = 0
                elif grid[i][j] == 2:
                    butti[i][j] = 1
                    queue.append((i, j))
        
        if len(queue) == 0:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return 0

        while queue:
            (p, q) = queue.popleft()

            cost = butti[p][q]
            for i in range(4):
                nrow = p + row[i]
                ncol = q + col[i]

                if 0 <= nrow < row_max and 0 <= ncol < col_max and butti[nrow][ncol] == 0:
                    butti[nrow][ncol] = cost + 1
                    queue.append((nrow,ncol))
            
        min_time = float("-inf")
        for i in range(len(butti)):
            for j in range(len(butti[0])):
                if butti[i][j] == 0:
                    return -1
                min_time = max(min_time, butti[i][j])

        return min_time - 1
        """
        dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        row_max = len(grid)
        col_max = len(grid[0])
        queue = deque()
        good_oranges = 0
        min_time = 0

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                if grid[r][c] == 1:
                    good_oranges += 1
        
        if not queue and good_oranges > 0:
            return -1
        
        while queue:
            r, c, t = queue.popleft()

            min_time = max(min_time, t)

            for d in dir:
                nr = r + d[0]
                nc = c + d[1]

                if (0 <= nr < row_max and
                    0 <= nc < col_max and
                    grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    good_oranges -= 1
                    queue.append((nr, nc, t + 1))
        
        if good_oranges:
            return -1
        
        return min_time
