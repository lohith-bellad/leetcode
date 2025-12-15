class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        row_max = len(board)
        col_max = len(board[0])

        visited = [[0 for i in range(col_max)] for i in range(row_max)]

        def dfs(r: int, c: int, ind: int) -> bool:
            if ind == len(word):
                return True

            res = False
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]

                if (
                    0 <= nr < row_max
                    and 0 <= nc < col_max
                    and board[nr][nc] == word[ind]
                    and visited[nr][nc] == 0
                ):
                    visited[nr][nc] = 1
                    res = res or dfs(nr, nc, ind + 1)
                    visited[nr][nc] = 0
            return res

        for i in range(row_max):
            for j in range(col_max):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i, j, 1) == True:
                        return True
                    visited[i][j] = 0

        return False
