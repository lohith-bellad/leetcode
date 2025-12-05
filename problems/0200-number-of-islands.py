"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3


Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 300
    * grid[i][j] is '0' or '1'.

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        row_max = len(grid)
        col_max = len(grid[0])

        queue = deque()
        cur_idx = 1

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == "1":
                    cur_idx += 1
                    queue.append((r, c))
                    grid[r][c] = str(cur_idx)

                    while queue:
                        row, col = queue.popleft()

                        for d in dirs:
                            nrow = row + d[0]
                            ncol = col + d[1]

                            if (
                                0 <= nrow < row_max
                                and 0 <= ncol < col_max
                                and grid[nrow][ncol] == "1"
                            ):
                                queue.append((nrow, ncol))
                                grid[nrow][ncol] = str(cur_idx)

        return cur_idx - 1
