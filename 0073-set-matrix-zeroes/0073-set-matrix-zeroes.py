class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col = False

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                first_col = True
                break

        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
        
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        if first_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0
