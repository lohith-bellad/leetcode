class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        my_stack = []
        output = [0 for i in range(len(heights))]

        for i in range(len(heights) - 1, -1, -1):
            while my_stack and my_stack[-1] <= heights[i]:
                my_stack.pop()
                output[i] += 1
            if my_stack:
                output[i] += 1
            my_stack.append(heights[i])
        
        return output
        """
        hstack = [heights[-1]]
        output = [0]

        for i in range(len(heights) - 2, -1, -1):
            count = 0
            while hstack and hstack[-1] <= heights[i]:
                hstack.pop()
                count += 1
            if hstack:
                count += 1
            output.append(count)
            hstack.append(heights[i])
        
        output.reverse()

        return output