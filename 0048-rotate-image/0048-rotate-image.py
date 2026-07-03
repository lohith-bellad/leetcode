class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        n = len(matrix)

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
        
        return
        """
        n = len(matrix)

        for row in range(n // 2):
            for col in range((n + 1) // 2):
                temp = matrix[row][col]
                matrix[row][col] = matrix[n - col - 1][row]
                matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1]
                matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
                matrix[col][n - row - 1] = temp
        
        return
            


