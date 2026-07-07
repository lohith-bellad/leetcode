class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        size = len(grid)

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        island_map = {}
        island_idx = 2

        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = island_idx

                island_size = 1
                while len(queue) > 0:
                    row, col = queue.popleft()

                    for d in dirs:
                        nrow = row + d[0]
                        ncol = col + d[1]

                        if 0 <= nrow < size and 0 <= ncol < size and grid[nrow][ncol] == 1:
                            queue.append((nrow, ncol))
                            grid[nrow][ncol] = island_idx
                            island_size += 1
                
                island_map[island_idx] = island_size
                island_idx += 1

        max_island_size = 0
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 0:
                    cur_size = 0
                    island_set = set()

                    for d in dirs:
                        new_i = i + d[0]
                        new_j = j + d[1]

                        if 0 <= new_i < size and 0 <= new_j < size and grid[new_i][new_j] != 0 and grid[new_i][new_j] not in island_set:
                            island_set.add(grid[new_i][new_j])
                            cur_size += island_map[grid[new_i][new_j]]
                    
                    max_island_size = max(max_island_size, cur_size + 1)
        
        if max_island_size == 0:
            return island_map[2]
        
        return max_island_size
        """
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(grid)
        col_max = len(grid[0])
        queue = deque()
        island_sizes = {}
        ind = 1

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == 1:
                    ind += 1
                    grid[r][c] = ind
                    queue.append((r, c))
                    cur_count = 1

                    while queue:
                        row, col = queue.popleft()

                        for d in dir:
                            nrow = row + d[0]
                            ncol = col + d[1]

                            if (0 <= nrow < row_max and
                                0 <= ncol < col_max and
                                grid[nrow][ncol] == 1):
                                grid[nrow][ncol] = ind
                                cur_count += 1
                                queue.append((nrow, ncol))

                    island_sizes[ind] = cur_count
        
        max_area = float("-inf")

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == 0:
                    cur_max_area = 0
                    islands_done = set()

                    for d in dir:
                        nr = r + d[0]
                        nc = c + d[1]

                        if (0 <= nr < row_max and
                            0 <= nc < col_max and
                            grid[nr][nc] not in islands_done and
                            grid[nr][nc] > 1):
                            islands_done.add(grid[nr][nc])
                            cur_max_area += island_sizes[grid[nr][nc]]
                    
                    max_area = max(max_area, cur_max_area + 1)
        
        if max_area == float("-inf"):
            return island_sizes[2]
        
        return max_area

