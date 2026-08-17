class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        row_max = len(grid)
        col_max = len(grid[0])
        min_heap = []
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited.add((0, 0))

        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if row == row_max - 1 and col == col_max - 1:
                return time
            
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if nrow < 0 or nrow >= row_max or ncol < 0 or ncol >= col_max or (nrow, ncol) in visited:
                    continue
                
                heapq.heappush(min_heap, (max(time, grid[nrow][ncol]),nrow, ncol))
                visited.add((nrow, ncol))
        
        return -1
        """
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(grid)
        col_max = len(grid[0])

        def can_swim(t):
            queue = deque()
            queue.append((0, 0))
            visited = set()
            visited.add((0, 0))

            while queue:
                row, col = queue.popleft()

                if row == row_max - 1 and col == col_max - 1:
                    return True

                for d in dirs:
                    nrow = row + d[0]
                    ncol = col + d[1]

                    if (0 <= nrow < row_max and
                        0 <= ncol < col_max and
                        (nrow, ncol) not in visited and
                        grid[nrow][ncol] <= t):
                        queue.append((nrow, ncol))
                        visited.add((nrow, ncol))

            return False

        n = len(grid)
        start = max(grid[0][0], grid[n - 1][n - 1])
        end = n * n - 1

        while start < end:
            mid = start + (end - start) // 2

            if can_swim(mid):
                end = mid
            else:
                start = mid + 1

        return start