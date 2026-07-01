class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        box_set = [set() for i in range(9)]
        to_fill = []

        def get_box_ind(row, col):
            return (row // 3) * 3 + (col // 3)
        
        def traverse(ind):
            if ind == len(to_fill):
                return True
            
            row, col = to_fill[ind]
            box_ind = get_box_ind(row, col)
            for d in range(1, 10):
                if d in row_set[row] or d in col_set[col] or d in box_set[box_ind]:
                    continue
                
                row_set[row].add(d)
                col_set[col].add(d)
                box_set[box_ind].add(d)
                board[row][col] = str(d)

                if traverse(ind + 1):
                    return True

                row_set[row].remove(d)
                col_set[col].remove(d)
                box_set[box_ind].remove(d)
                board[row][col] = "."
            
            return False

        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    to_fill.append((r, c))
                else:
                    row_set[r].add(int(board[r][c]))
                    col_set[c].add(int(board[r][c]))
                    box_set[get_box_ind(r, c)].add(int(board[r][c]))
        
        traverse(0)
        return