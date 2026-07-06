class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_max = len(image)
        col_max = len(image[0])
        queue = deque()
        pivot = image[sr][sc]
        image[sr][sc] = color
        queue.append((sr, sc))

        while queue:
            row, col = queue.popleft()

            for d in dir:
                nrow = row + d[0]
                ncol = col + d[1]

                if (0 <= nrow < row_max and
                    0 <= ncol < col_max and
                    image[nrow][ncol] == pivot):
                    image[nrow][ncol] = color
                    queue.append((nrow, ncol))
        
        return image
