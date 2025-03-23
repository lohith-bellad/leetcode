class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = []
        count = 0

        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            transpose.append(temp)
        
        for row in grid:
            for col in transpose:
                if row == col:
                    count += 1

        return count