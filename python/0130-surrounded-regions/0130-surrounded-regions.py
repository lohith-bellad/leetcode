class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(row: int, col: int) -> bool:
            for d in dirs:
                nr = row + d[0]
                nc = col + d[1]

                if (
                    0 <= nr < row_max
                    and 0 <= nc < col_max
                    and board[nr][nc] == "O"
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    dfs(nr, nc)

        row_max = len(board)
        col_max = len(board[0])

        visited = set()

        for i in range(col_max):
            if board[0][i] == "O" and (0, i) not in visited:
                visited.add((0, i))
                dfs(0, i)

            if board[row_max - 1][i] == "O" and (row_max - 1, i) not in visited:
                visited.add((row_max - 1, i))
                dfs(row_max - 1, i)

        for i in range(row_max):
            if board[i][0] == "O" and (i, 0) not in visited:
                visited.add((i, 0))
                dfs(i, 0)

            if board[i][col_max - 1] == "O" and (i, col_max - 1) not in visited:
                visited.add((i, col_max - 1))
                dfs(i, col_max - 1)

        for r in range(row_max):
            for c in range(col_max):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"

        return
