class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_max = len(matrix)
        col_max = len(matrix[0])
    
        rows = set()
        cols = set()
    
        for i in range(row_max):
            for j in range(col_max):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in rows:
            for j in range(col_max):
                matrix[row][j] = 0
        
        for col in cols:
            for i in range(row_max):
                matrix[i][col] = 0
        
        return