# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        
        def dfs(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()

            for i in range(len(dirs)):
                new_dir = (d + i) % len(dirs)
                new_pos_x = cell[0] + dirs[new_dir][0]
                new_pos_y = cell[1] + dirs[new_dir][1]

                if (new_pos_x, new_pos_y) in visited or not robot.move():
                    robot.turnRight()
                    continue

                dfs((new_pos_x, new_pos_y), new_dir)
                robot.turnRight()

            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()               

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()
        dfs()
        return
        """
        def dfs(r, c, d):
            robot.clean()

            for i in range(4):
                new_d = (d + i) % 4
                new_r = r + dirs[new_d][0]
                new_c = c + dirs[new_d][1]

                if (new_r, new_c) in visited or not robot.move():
                    robot.turnRight()
                    continue

                visited.add((new_r, new_c))
                dfs(new_r, new_c, new_d)
                robot.turnRight()

            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()
        visited.add((0, 0))
        dfs(0, 0, 0)
        return