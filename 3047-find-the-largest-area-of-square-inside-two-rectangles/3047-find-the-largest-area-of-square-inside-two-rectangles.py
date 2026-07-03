class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        largest_side = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                width = min(topRight[i][0], topRight[j][0]) - max(
                    bottomLeft[i][0], bottomLeft[j][0] 
                )
                height = min(topRight[i][1], topRight[j][1]) - max(
                    bottomLeft[i][1], bottomLeft[j][1] 
                )

                if width > 0 and height > 0:
                    largest_side = max(largest_side, min(width, height))
        
        return largest_side**2