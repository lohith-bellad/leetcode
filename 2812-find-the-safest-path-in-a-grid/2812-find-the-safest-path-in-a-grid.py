class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        row_max = len(grid)
        col_max = len(grid[0])
        queue = deque()

        for i in range(row_max):
            for j in range(col_max):
                if grid[i][j] == 1:
                    queue.append((i, j, 1))
        
        while queue:
            r, c, m = queue.popleft()

            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]

                if 0 <= nr < row_max and 0 <= nc < col_max and grid[nr][nc] == 0:
                    grid[nr][nc] = m + 1
                    queue.append((nr, nc, m + 1))
        
        max_heap = [(-grid[0][0], 0, 0)]
        safeness = float('inf')
        visited = set()
        visited.add((0, 0))

        while max_heap:
            sf, r, c = heapq.heappop(max_heap)

            safeness = min(safeness, -sf)

            if r == row_max - 1 and c == col_max - 1:
                return safeness - 1

            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]

                if 0 <= nr < row_max and 0 <= nc < col_max and (nr, nc) not in visited:
                    heapq.heappush(max_heap, (-grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
        
        return 0