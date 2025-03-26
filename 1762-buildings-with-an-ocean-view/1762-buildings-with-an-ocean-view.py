class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        my_stack = []

        for i in range(len(heights)):
            while len(my_stack) > 0 and heights[my_stack[-1]] <= heights[i]:
                my_stack.pop()
            my_stack.append(i)
        
        return my_stack