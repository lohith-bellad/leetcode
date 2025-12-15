class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seq_num = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        row_max = len(grid)
        col_max = len(grid[0])

        for i in range(row_max):
            for j in range(col_max):
                if grid[i][j] == "1":
                    seq_num += 1
                    grid[i][j] = str(seq_num)
                    queue.append((i, j))

                while len(queue) > 0:
                    (r, c) = queue.popleft()

                    for d in dirs:
                        new_r = r + d[0]
                        new_c = c + d[1]

                        if (
                            0 <= new_r < row_max
                            and 0 <= new_c < col_max
                            and grid[new_r][new_c] == "1"
                        ):
                            grid[new_r][new_c] = str(seq_num)
                            queue.append((new_r, new_c))

        return seq_num - 1
