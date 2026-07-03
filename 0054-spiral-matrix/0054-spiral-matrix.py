class Solution(object):
    def spiralOrder(self, matrix):
        dir = 0
        row_min = 0
        row_max = len(matrix) - 1
        col_min = 0
        col_max = len(matrix[0]) - 1
        output = []

        while row_min <= row_max and col_min <= col_max:
            # Row traverse
            if dir % 2 == 0:
                if dir == 0:
                    for col in range(col_min, col_max + 1):
                        output.append(matrix[row_min][col])
                    row_min += 1
                elif dir == 2:
                    for col in range(col_max, col_min - 1, -1):
                        output.append(matrix[row_max][col])
                    row_max -= 1
            # Col traverse
            else:
                if dir == 1:
                    for row in range(row_min, row_max + 1):
                        output.append(matrix[row][col_max])
                    col_max -= 1
                elif dir == 3:
                    for row in range(row_max, row_min - 1, -1):
                        output.append(matrix[row][col_min])
                    col_min += 1
            
            dir = (dir + 1) % 4
        
        return output