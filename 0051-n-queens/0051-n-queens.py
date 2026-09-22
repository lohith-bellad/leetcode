class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def traverse(row, cols, diag, rev_diag, mat):
            if row >= n:
                temp = []
                for r in mat:
                    temp.append("".join(r))
                output.append(temp)
                return
            
            for col in range(n):
                d = row + col
                rd = row - col

                if col not in cols and d not in diag and rd not in rev_diag:
                    mat[row][col] = "Q"
                    cols.add(col)
                    diag.add(d)
                    rev_diag.add(rd)

                    traverse(row + 1, cols, diag, rev_diag, mat)

                    cols.remove(col)
                    diag.remove(d)
                    rev_diag.remove(rd)
                    mat[row][col] = "."

        output = []
        mat = [["." for i in range(n)] for i in range(n)]
        traverse(0, set(), set(), set(), mat)

        return output