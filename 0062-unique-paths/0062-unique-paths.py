class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        memo = [[0 for i in range(n)] for i in range(m)]

        def find(memo: [[]], x: int, y: int) -> int:
            if x == 0 and y == 0:
                return 1

            top = left = 0
            if memo[x][y] == 0:
                if x - 1 >= 0:
                    top = find(memo, x - 1, y)
                if y - 1 >= 0:
                    left = find(memo, x, y - 1)
            
                memo[x][y] = top + left

            return memo[x][y]

        return find(memo, m - 1, n -1)
        """
        def dfs(row: int, col: int) -> int:
            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in self.cache:
                return self.cache[(row, col)]

            down = 0
            if row + 1 < m:
                down = dfs(row + 1, col)

            side = 0
            if col + 1 < n:
                side = dfs(row, col + 1)

            self.cache[(row, col)] = (down + side)
            return self.cache[(row, col)]
    
        self.cache = {}
        return dfs(0, 0)
        """
        dirs = [[-1, 0], [0, -1]]

        def dfs(row, col):
            if row == 0 and col == 0:
                return 1

            if (row, col) in cache:
                return cache[(row, col)]
            
            cur_count = 0
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if 0 <= nrow < m and 0 <= ncol < n:
                    cur_count += dfs(nrow, ncol)

            cache[(row, col)] = cur_count 
            return cur_count

        cache = {}
        return dfs(m - 1, n - 1)
        """