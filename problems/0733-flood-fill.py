"""
733. Flood Fill
Easy

An image is represented by an m x n integer grid image where image[i][j] represents
the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill
on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel, plus
any pixels connected 4-directionally to those pixels (also with the same color), and
so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.


Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1), all
    pixels connected by a path of the same color as the starting pixel (i.e., the
    blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally
    connected to the starting pixel.

Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to
    the image.


Constraints:
    * m == image.length
    * n == image[i].length
    * 1 <= m, n <= 50
    * 0 <= image[i][j], color < 2^16
    * 0 <= sr < m
    * 0 <= sc < n

"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        row_max = len(image)
        col_max = len(image[0])
        queue = deque()
        visited = set()

        init_color = image[sr][sc]
        queue.append((sr, sc))
        visited.add((sr, sc))
        image[sr][sc] = color

        while queue:
            row, col = queue.popleft()

            for d in dirs:
                nrow = row + d[0]
                ncol = col + d[1]

                if (
                    0 <= nrow < row_max
                    and 0 <= ncol < col_max
                    and (nrow, ncol) not in visited
                    and image[nrow][ncol] == init_color
                ):
                    image[nrow][ncol] = color
                    visited.add((nrow, ncol))
                    queue.append((nrow, ncol))

        return image
