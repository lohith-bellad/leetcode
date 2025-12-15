class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def traverse(queue, row_max, col_max):
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            output = set()
            while len(queue) > 0:
                r, c = queue.popleft()
                output.add((r, c))

                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]

                    if (
                        0 <= nr < row_max
                        and 0 <= nc < col_max
                        and (nr, nc) not in output
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        queue.append((nr, nc))

            return output

        row_max = len(heights)
        col_max = len(heights[0])

        p_queue = deque()
        a_queue = deque()

        for i in range(row_max):
            p_queue.append((i, 0))
            a_queue.append((i, col_max - 1))

        for i in range(col_max):
            p_queue.append((0, i))
            a_queue.append((row_max - 1, i))

        p_regions = traverse(p_queue, row_max, col_max)
        a_regions = traverse(a_queue, row_max, col_max)

        return list(p_regions & a_regions)
