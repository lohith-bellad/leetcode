class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(grid)
        col_max = len(grid[0])
        seq_num = 1
        queue = deque()

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == "1":
                    seq_num += 1
                    grid[r][c] = str(seq_num)
                    queue.append((r, c))

                    while queue:
                        row, col = queue.popleft()

                        for d in dir:
                            nrow = row + d[0]
                            ncol = col + d[1]

                            if (0 <= nrow < row_max and
                                0 <= ncol < col_max and
                                grid[nrow][ncol] == "1"):
                                grid[nrow][ncol] = str(seq_num)
                                queue.append((nrow, ncol))
        
        return seq_num - 1
