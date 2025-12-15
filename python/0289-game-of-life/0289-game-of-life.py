class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_indices = [0, 0, 1, 1, 1, -1, -1, -1]
        col_indices = [-1, 1, -1, 0, 1, -1, 0, 1]

        row_max = len(board)
        col_max = len(board[0])

        for r in range(row_max):
            for c in range(col_max):
                count = 0

                for i in range(len(row_indices)):
                    new_row = r + row_indices[i]
                    new_col = c + col_indices[i]

                    if 0 <= new_row < row_max and 0 <= new_col < col_max:
                        if board[new_row][new_col] > 0:
                            count += 1

                if board[r][c] <= 0 and count == 3:
                    board[r][c] = -1
                elif board[r][c] > 0 and (count > 3 or count < 2):
                    board[r][c] = 2

        for r in range(row_max):
            for c in range(col_max):
                if board[r][c] == -1:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 0

        return
