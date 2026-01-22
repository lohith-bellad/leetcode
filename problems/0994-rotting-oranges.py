"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:
    * 0 representing an empty cell,
    * 1 representing a fresh orange, or
    * 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange. If this is impossible, return -1.


Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 10
    * grid[i][j] is 0, 1, or 2.

"""

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])
        butti = [[-1 for _ in range(col_max)] for _ in range(row_max)]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        fresh_orange_present = False

        for i in range(row_max):
            for j in range(col_max):
                if grid[i][j] == 1:
                    butti[i][j] = 0
                    fresh_orange_present = True
                elif grid[i][j] == 2:
                    butti[i][j] = 1
                    queue.append((i, j))

        if not queue and fresh_orange_present:
            return -1

        while queue:
            row, col = queue.popleft()

            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if (
                    0 <= nrow < row_max
                    and 0 <= ncol < col_max
                    and butti[nrow][ncol] == 0
                ):
                    butti[nrow][ncol] = butti[row][col] + 1
                    queue.append((nrow, ncol))

        min_time = 0

        for i in range(row_max):
            for j in range(col_max):
                if butti[i][j] == 0:
                    return -1
                min_time = max(min_time, butti[i][j])

        return min_time - 1
