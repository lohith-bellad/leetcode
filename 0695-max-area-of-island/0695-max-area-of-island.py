class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        row_max = len(grid)
        col_max = len(grid[0])
        max_island = 0
        queue = deque()

        for i in range(row_max):
            for j in range(col_max):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 2

                    cnt = 1
                    while len(queue) > 0:
                        r, c = queue.popleft()

                        for d in dirs:
                            nr = r + d[0]
                            nc = c + d[1]

                            if 0 <= nr < row_max and 0 <= nc < col_max and grid[nr][nc] == 1:
                                queue.append((nr, nc))
                                grid[nr][nc] = 2
                                cnt += 1
                    
                    max_island = max(max_island, cnt)
        
        return max_island
