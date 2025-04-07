class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def find_slope(p1, p2) -> int:
            x1, y1 = p1
            x2, y2 = p2

            if x2 - x1 == 0:
                return inf

            return (y2 - y1) / (x2 - x1)

        if len(points) <= 2:
            return len(points)
        
        res = 1
        i = 0

        while i < len(points):
            table = {}
            j = i + 1
            while j < len(points):
                p1 = points[i]
                p2 = points[j]

                slope = find_slope(p1, p2)
                table[slope] = table.get(slope, 0) + 1
                res = max(res, table[slope])
                j += 1
            i += 1
        
        return res + 1

        