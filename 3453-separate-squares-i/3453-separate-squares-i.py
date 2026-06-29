class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_below(y: float) -> float:
            area = 0.0

            for _, yi, h in squares:
                ylen = min(float(h), max(0.0, y - yi))
                area += ylen * h
            
            return area
        
        total_area = 0.0
        min_y = float("inf")
        max_y = float("-inf")

        for _, y, h in squares:
            total_area += h * h
            min_y = min(min_y, y)
            max_y = max(max_y, y + h)
        
        target_area = total_area / 2.0

        for i in range(50):
            mid = min_y + (max_y - min_y) / 2.0

            a = area_below(mid)
            if a < target_area:
                min_y = mid
            else:
                max_y = mid
        
        return min_y