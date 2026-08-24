class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        points.sort()
        stack = []
        stack.append(points[0])
        
        for i in range(1, len(points)):
            new = points[i]
            old = stack.pop()

            if old[0] <= new[0] < old[1]:
                if new[1] <= old[1]:
                    stack.append([new[0], new[1]])
                else:
                    stack.append([new[0], old[1]])
            elif new[0] == old[1]:
                stack.append([new[0], new[0]])
            else:
                stack.append(old)
                stack.append(new)
           
        return len(stack)
        """
        points.sort()
        output = []

        for new_x, new_y in points:
            if not output:
                output.append([new_x, new_y])
            else:
                old_x, old_y = output[-1]
                if old_x <= new_x <= old_y:
                    output.pop()
                    new_x = max(old_x, new_x)
                    new_y = min(old_y, new_y)
                output.append([new_x, new_y])

        return len(output)