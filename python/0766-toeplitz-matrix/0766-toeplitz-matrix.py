class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_max = len(matrix)
        col_max = len(matrix[0])
        map = {}

        for r in range(row_max):
            for c in range(col_max):
                if (r - c) not in map:
                    map[r - c] = matrix[r][c]
                elif map[r - c] != matrix[r][c]:
                    return False

        return True
