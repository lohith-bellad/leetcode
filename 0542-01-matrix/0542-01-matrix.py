class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(mat)
        col_max = len(mat[0])
        queue = deque()
        visited = set()

        for r in range(row_max):
            for c in range(col_max):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            r, c, dist = queue.popleft()

            for d in dir:
                nr = r + d[0]
                nc = c + d[1]

                if (0 <= nr < row_max and
                    0 <= nc < col_max and
                    mat[nr][nc] == 1 and
                    (nr, nc) not in visited):
                    mat[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))
        
        return mat