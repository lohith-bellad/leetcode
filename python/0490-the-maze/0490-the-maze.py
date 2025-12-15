class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        row_max = len(maze)
        col_max = len(maze[0])

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row: int, col: int, visited: {}) -> bool:
            if (row, col) in visited:
                return False

            if row == destination[0] and col == destination[1]:
                return True

            visited.add((row, col))

            for d in dirs:
                nrow = row
                ncol = col

                while (
                    0 <= nrow < row_max
                    and 0 <= ncol < col_max
                    and maze[nrow][ncol] == 0
                ):
                    nrow += d[0]
                    ncol += d[1]
                nrow -= d[0]
                ncol -= d[1]

                if dfs(nrow, ncol, visited):
                    return True

            return False

        visited = set()
        return dfs(start[0], start[1], visited)
