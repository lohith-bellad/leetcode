"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.


Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false


Constraints:
    * m == board.length
    * n == board[i].length
    * 1 <= m, n <= 6
    * 1 <= word.length <= 15
    * board and word consists of only lowercase and uppercase English letters

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row_max = len(board)
        col_max = len(board[0])
        visited = set()

        def dfs(row, col, ind):
            if ind >= len(word):
                return True

            for dir in dirs:
                nrow = row + dir[0]
                ncol = col + dir[1]

                if (
                    0 <= nrow < row_max
                    and 0 <= ncol < col_max
                    and (nrow, ncol) not in visited
                    and board[nrow][ncol] == word[ind]
                ):
                    visited.add((nrow, ncol))
                    if dfs(nrow, ncol, ind + 1):
                        return True
                    visited.remove((nrow, ncol))

            return False

        for r in range(row_max):
            for c in range(col_max):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    if dfs(r, c, 1):
                        return True
                    visited.remove((r, c))

        return False
