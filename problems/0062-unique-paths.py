"""
62. Unique Paths
Medium

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal
to 2 * 10^9.


Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach
        the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down


Constraints:
    * 1 <= m, n <= 100

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0, 1], [1, 0]]

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in cache:
                return cache[(row, col)]

            paths = 0
            for dir in dirs:
                nrow = row + dir[0]
                ncol = col + dir[1]

                if 0 <= nrow < m and 0 <= ncol < n:
                    paths += dfs(nrow, ncol)

            cache[(row, col)] = paths
            return cache[(row, col)]

        cache = {}
        return dfs(0, 0)
