class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        my_stack = []
        output = []

        for i in range(len(heights)):
            my_stack.append((heights[i], i))
        
        block = 0
        while len(my_stack) > 0:
            building, idx = my_stack.pop()
            if building > block:
                output.append(idx)
                block = building
        
        output.reverse()
        return output