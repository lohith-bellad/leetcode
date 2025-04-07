class Solution:
    def maxDepth(self, s: str) -> int:
        my_stack = []
        output = 0

        for c in s:
            if c == "(":
                my_stack.append(c)
                output = max(output, len(my_stack))
            elif c == ")":
                my_stack.pop()
        
        return output