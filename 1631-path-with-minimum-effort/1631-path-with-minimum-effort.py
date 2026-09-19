class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row_max = len(heights)
        col_max = len(heights[0])
        cache = {}
        heap = [(0, 0, 0)]

        while heap:
            e, row, col = heapq.heappop(heap)

            if row == row_max - 1 and col == col_max - 1:
                return e
            
            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if 0 <= nrow < row_max and 0 <= ncol < col_max:
                    diff = abs(heights[row][col] - heights[nrow][ncol])
                    res = max(e, diff)
                    if res < cache.get((nrow, ncol), float('inf')):
                        cache[(nrow, ncol)] = res
                        heapq.heappush(heap, (res, nrow, ncol))
        
        return 0