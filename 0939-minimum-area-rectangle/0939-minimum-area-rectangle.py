class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pset = set()
        area = float("inf")

        for x, y in points:
            pset.add((x, y))

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                if x2 == x1 or y2 == y1:
                    continue
                
                if (x2, y1) in pset and (x1, y2) in pset:
                    area = min(area, abs(x1 - x2) * abs(y2 - y1))
        
        if area == float("inf"):
            return 0

        return area