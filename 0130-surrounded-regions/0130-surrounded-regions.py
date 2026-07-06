class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row, col):
            for d in dir:
                nrow = row + d[0]
                ncol = col + d[1]

                if (0 <= nrow < row_max and
                    0 <= ncol < col_max and
                    board[nrow][ncol] == "O" and
                    (nrow, ncol) not in visited):
                    visited.add((nrow, ncol))
                    dfs(nrow, ncol)
            return

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(board)
        col_max = len(board[0])
        visited = set()

        for col in range(col_max):
            if board[0][col] == "O" and (0, col) not in visited:
                visited.add((0, col))
                dfs(0, col)
        
            if board[row_max - 1][col] == "O" and (row_max - 1, col) not in visited:
                visited.add((row_max - 1, col))
                dfs(row_max - 1, col)
        
        for row in range(row_max):
            if board[row][0] == "O" and (row, 0) not in visited:
                visited.add((row, 0))
                dfs(row, 0)

            if board[row][col_max - 1] == "O" and (row, col_max - 1) not in visited:
                visited.add((row, col_max - 1))
                dfs(row, col_max - 1)
        
        for r in range(row_max):
            for c in range(col_max):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        
        return