class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        output = [[0 for i in range(m)] for i in range(n)]

        for row in range(m):
            for col in range(n):
                output[col][row] = matrix[row][col]
        
        return output