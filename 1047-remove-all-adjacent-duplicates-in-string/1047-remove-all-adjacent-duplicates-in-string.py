class Solution:
    def removeDuplicates(self, s: str) -> str:
        my_stack = []

        for c in s:
            if my_stack:
                if c == my_stack[-1]:
                    my_stack.pop()
                else:
                    my_stack.append(c)
            else:
                my_stack.append(c)
        
        return "".join(my_stack)