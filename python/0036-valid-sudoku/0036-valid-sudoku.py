class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {}
        col_hash = {}

        for r in range(9):
            row_hash.clear()
            col_hash.clear()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in row_hash:
                        row_hash[board[r][c]] = 1
                    else:
                        return False
                if board[c][r] != ".":
                    if board[c][r] not in col_hash:
                        col_hash[board[c][r]] = 1
                    else:
                        return False

        for outer_row in range(0, 9, 3):
            for outer_col in range(0, 9, 3):
                row_hash.clear()
                for r in range(outer_row, outer_row + 3):
                    for c in range(outer_col, outer_col + 3):
                        if board[r][c] != ".":
                            if board[r][c] not in row_hash:
                                row_hash[board[r][c]] = 1
                            else:
                                return False

        return True
