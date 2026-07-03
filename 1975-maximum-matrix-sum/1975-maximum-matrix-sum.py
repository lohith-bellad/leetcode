class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        smallest = float("inf")
        total = 0
        neg_count = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] < 0:
                    neg_count += 1
                total += abs(matrix[row][col])
                smallest = min(smallest, abs(matrix[row][col]))

        if neg_count % 2 == 1:
            total -= 2*smallest
        
        return total