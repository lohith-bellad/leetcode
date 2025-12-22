"""
827. Making A Large Island
Hard

You are given an n x n binary matrix grid. You are allowed to change at most
one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.


Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island
        with area = 3.

Example 2:
    Input: grid = [[1,1],[1,0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island
        with area = 4.

Example 3:
    Input: grid = [[1,1],[1,1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:
    * n == grid.length
    * n == grid[i].length
    * 1 <= n <= 500
    * grid[i][j] is either 0 or 1.

"""

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_size = {}
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row_max = len(grid)
        col_max = len(grid[0])
        island_idx = 1
        queue = deque()

        for i in range(row_max):
            for j in range(col_max):
                if grid[i][j] == 1:
                    island_idx += 1
                    queue.append((i, j))
                    grid[i][j] = island_idx
                    cur_island_size = 1

                    while queue:
                        r, c = queue.popleft()

                        for dir in dirs:
                            nr = r + dir[0]
                            nc = c + dir[1]

                            if (
                                0 <= nr < row_max
                                and 0 <= nc < col_max
                                and grid[nr][nc] == 1
                            ):
                                queue.append((nr, nc))
                                grid[nr][nc] = island_idx
                                cur_island_size += 1

                    island_size[island_idx] = cur_island_size

        max_size = 0
        for i in range(row_max):
            for j in range(col_max):
                if grid[i][j] == 0:
                    cur_size = 0
                    island_visited = set()
                    for dir in dirs:
                        ni = i + dir[0]
                        nj = j + dir[1]

                        if (
                            0 <= ni < row_max
                            and 0 <= nj < col_max
                            and grid[ni][nj] > 1
                            and grid[ni][nj] not in island_visited
                        ):
                            island_visited.add(grid[ni][nj])
                            cur_size += island_size[grid[ni][nj]]

                    max_size = max(cur_size + 1, max_size)

        # If grid is all ones, return size of first island
        if max_size == 0:
            return island_size[2]

        return max_size
