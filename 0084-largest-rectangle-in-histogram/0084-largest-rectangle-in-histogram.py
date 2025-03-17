class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hstack = []
        max_area = 0

        for i in range(len(heights)):
            start = i
            while hstack and hstack[-1][1] > heights[i]:
                ind, height = hstack.pop()
                max_area = max(max_area, (height * (i - ind)))
                start = ind
            hstack.append((start, heights[i]))
        
        while len(hstack) > 0:
            ind, height = hstack.pop()
            max_area = max(max_area, height * (len(heights) - ind))
        
        return max_area

        