class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def diag_elems(mat: List[List[int]], start: int, end: int) -> List[int]:
            output = []
            idx = start
            i = 1
            while idx < end:
                output.append(mat[idx][end - i])
                idx += 1
                i += 1
            return output
        
        res = []
        row_max = len(mat)
        col_max = len(mat[0])
        min_side = min(row_max, col_max)

        if min_side == 1:
            if row_max == 1:
                return mat[0]
            else:
                for r in range(row_max):
                    res.append(mat[r][0])
                return res

        for size in range(1,  min_side + 1):
            res.append(diag_elems(mat, 0, size))
        
        if row_max > col_max:
            c = 1
            new_mat = mat
            while c + min_side <= row_max:
                new_mat = new_mat[1:]
                res.append(diag_elems(new_mat, 0, len(new_mat[0])))
                c += 1
        else:   
            c = 1
            new_mat = mat
            while c + min_side <= col_max:
                new_mat = [row[c:] for row in mat]
                res.append(diag_elems(new_mat, 0, len(new_mat[0])))
                c += 1
        
        for offset in range(1, len(new_mat[0])):
            res.append(diag_elems(new_mat, offset, len(new_mat)))
        
        i = 1
        while i < len(res):
            if i % 2 == 0:
                res[i].reverse()
            i += 1
        
        out = []
        for r in res:
            out += r
        
        return out
       
