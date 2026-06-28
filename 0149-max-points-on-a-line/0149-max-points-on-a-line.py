class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
    
        max_points = 1

        for pivot in range(len(points) - 1):
            slopes = {}
            for point in range(pivot + 1, len(points)):
                x1, y1 = points[pivot]
                x2, y2 = points[point]

                if x2 - x1 == 0:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)

                slopes[slope] = slopes.get(slope, 0) + 1
                max_points = max(max_points, slopes[slope])
        
        return max_points + 1

        