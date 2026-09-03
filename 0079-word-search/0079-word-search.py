class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, ind):
            if ind >= len(word):
                return True

            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if (0 <= nrow < row_max and 
                    0 <= ncol < col_max and 
                    (nrow, ncol) not in visited and 
                    board[nrow][ncol] == word[ind]):
                    visited.add((nrow, ncol))
                    if dfs(nrow, ncol, ind + 1):
                        return True
                    visited.remove((nrow, ncol))

            return False

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(board)
        col_max = len(board[0])
        visited = set()

        for r in range(row_max):
            for c in range(col_max):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    if dfs(r, c, 1):
                        return True
                    visited.remove((r, c))

        return False