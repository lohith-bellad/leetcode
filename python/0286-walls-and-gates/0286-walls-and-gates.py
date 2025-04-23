class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
        row_max = len(rooms)
        col_max = len(rooms[0])
        empty_room = 2**31 - 1
        queue = deque()
    
        for r in range(row_max):
            for c in range(col_max):
                if rooms[r][c] == 0:
                    queue.append((r, c))
            
                while len(queue) > 0:
                    (row, col) = queue.popleft()
                
                    cur_dist = rooms[row][col]
                    for d in dirs:
                        nrow = row + d[0]
                        ncol = col + d[1]
                    
                        if 0 <= nrow < row_max and 0 <= ncol < col_max and (cur_dist + 1) < rooms[nrow][ncol] <= empty_room:
                            queue.append((nrow, ncol))
                            rooms[nrow][ncol] = cur_dist + 1
    
        return