class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
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
        """
        d_set = set()
        t_set = set()

        for r in range(9):
            d_set.clear()
            t_set.clear()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in d_set:
                        return False
                    d_set.add(board[r][c])

                if board[c][r] != ".":
                    if board[c][r] in t_set:
                        return False
                    t_set.add(board[c][r])

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):

                d_set.clear()
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in d_set:
                            return False
                        d_set.add(board[r][c])
        
        return True