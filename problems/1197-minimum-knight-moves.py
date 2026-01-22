"""
1197. Minimum Knight Moves
Medium

In an infinite chess board with coordinates from -infinity to +infinity, you
have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is
two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].
It is guaranteed the answer exists.


Example 1:
    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] -> [2, 1]

Example 2:
    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]


Constraints:
    * -300 <= x, y <= 300
    * 0 <= |x| + |y| <= 300

"""

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        queue = deque()
        visited = set()

        queue.append((0, 0, 0))
        visited.add((0, 0))

        while queue:
            px, py, steps = queue.popleft()

            if px == abs(x) and py == abs(y):
                return steps

            for d in dirs:
                nx = px + d[0]
                ny = py + d[1]

                if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))

        return -1
