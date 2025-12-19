"""
542. 01 Matrix
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:
    * m == mat.length
    * n == mat[i].length
    * 1 <= m, n <= 10^4
    * 1 <= m * n <= 10^4
    * mat[i][j] is either 0 or 1.
    * There is at least one 0 in mat.

"""

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue = deque()
        visited = set()
        row_max = len(mat)
        col_max = len(mat[0])

        for row in range(row_max):
            for col in range(col_max):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))

        while queue:
            r, c, dist = queue.popleft()

            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]

                if 0 <= nr < row_max and 0 <= nc < col_max and (nr, nc) not in visited:
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))
                    mat[nr][nc] = dist + 1

        return mat
