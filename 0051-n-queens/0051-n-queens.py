class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        def form_output(mat: []) -> []:
            out = []

            for row in mat:
                out.append("".join(row))
            
            return out

        def backtrack(row, diagonals, rev_diagonals, cols, mat):
            if row == n:
                output.append(form_output(mat))
                return

            for c in range(n):
                cur_diagonal = row - c
                cur_rev_diagonal = row + c

                if c not in cols and cur_diagonal not in diagonals and cur_rev_diagonal not in rev_diagonals:
                    mat[row][c] = "Q"
                    cols.add(c)
                    diagonals.add(cur_diagonal)
                    rev_diagonals.add(cur_rev_diagonal)

                    backtrack(row + 1, diagonals, rev_diagonals, cols, mat)

                    cols.remove(c)
                    diagonals.remove(cur_diagonal)
                    rev_diagonals.remove(cur_rev_diagonal)
                    mat[row][c] = "."


        ans = [["." for i in range(n)] for i in range(n)]
        output = []
        backtrack(0, set(), set(), set(), ans)
        return output
        """
        def traverse(row, cols, diag, rev_diag, mat):
            if row >= n:
                temp = []
                for r in mat:
                    temp.append("".join(r))
                output.append(temp)
            
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