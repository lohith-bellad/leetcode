class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_max = len(matrix) - 1
        while row_max >= 0 and matrix[row_max][0] > target:
            row_max -= 1
        
        col_max = len(matrix[0]) - 1
        while col_max >= 0 and matrix[0][col_max] > target:
            col_max -= 1
        
        for r in range(row_max + 1):
            for c in range(col_max + 1):
                if matrix[r][c] == target:
                    return True
        
        return False