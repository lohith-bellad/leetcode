class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_min = col_min = 0
        row_max = len(matrix)
        col_max = len(matrix[0])

        row = col = 0
        output = []
        while (row_min <= row < row_max) and (col_min <= col < col_max):
            while (col < col_max) and (row_min <= row < row_max):
                output.append(matrix[row][col])
                col += 1
            row_min += 1
            col -= 1
            row += 1

            while (row < row_max) and (col_min <= col < col_max):
                output.append(matrix[row][col])
                row += 1
            col_max -= 1
            row -= 1
            col -= 1

            while (col >= col_min) and (row_min <= row < row_max):
                output.append(matrix[row][col])
                col -= 1
            row_max -= 1
            col += 1
            row -= 1

            while (row >= row_min) and (col_min <= col < col_max):
                output.append(matrix[row][col])
                row -= 1
            col_min += 1
            row += 1
            col += 1

        return output
