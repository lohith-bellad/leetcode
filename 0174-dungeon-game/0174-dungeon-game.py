class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_max = len(dungeon)
        col_max = len(dungeon[0])
        dirs = [[0, 1], [1, 0]]

        def dfs(row, col):
            if row == row_max - 1 and col == col_max - 1:
                return max(1, 1 - dungeon[row][col])
            
            if (row, col) in cache:
                return cache[(row, col)]

            cur_min = float('inf')
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if 0 <= nrow < row_max and 0 <= ncol < col_max:
                    cur_min = min(cur_min, dfs(nrow, ncol) - dungeon[row][col])
            
            cache[(row, col)] = max(1, cur_min)
            return cache[(row, col)]
            
        cache = {}
        return dfs(0, 0)