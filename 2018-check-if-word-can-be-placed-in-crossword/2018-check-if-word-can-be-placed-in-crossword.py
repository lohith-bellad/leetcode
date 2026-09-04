class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def is_blocked(r, c):
            return not (0 <= r < row_max and 0 <= c < col_max) or board[r][c] == "#"
        
        def dfs(r, c, d):
            if not is_blocked(r - d[0], c - d[1]):
                return False

            for ch in word:
                if is_blocked(r, c) or board[r][c] not in (' ', ch):
                    return False

                r += d[0]
                c += d[1]

            return is_blocked(r, c)

        row_max = len(board)
        col_max = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(row_max):
            for c in range(col_max):
                for d in dirs:
                    if dfs(r, c, d):
                        return True

        return False
