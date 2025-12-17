"""
695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical).
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Example 1:
    Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected
        4-directionally.

Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0


Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 50
    * grid[i][j] is either 0 or 1.

"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        row_max = len(grid)
        col_max = len(grid[0])
        max_area = 0
        cur_area = 0
        queue = deque()
        visited = set()

        for r in range(row_max):
            for c in range(col_max):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))
                    cur_area = 1

                    while queue:
                        row, col = queue.popleft()

                        for d in dirs:
                            nrow = row + d[0]
                            ncol = col + d[1]

                            if (
                                0 <= nrow < row_max
                                and 0 <= ncol < col_max
                                and grid[nrow][ncol] == 1
                                and (nrow, ncol) not in visited
                            ):
                                queue.append((nrow, ncol))
                                visited.add((nrow, ncol))
                                cur_area += 1

                    max_area = max(max_area, cur_area)

        return max_area
