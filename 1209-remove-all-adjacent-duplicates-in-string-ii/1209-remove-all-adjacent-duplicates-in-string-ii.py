class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        my_stack = []

        for c in s:
            if my_stack and my_stack[-1][0] == c:
                my_stack[-1][1] += 1

                if my_stack[-1][1] >= k:
                    my_stack.pop()
            else:
                my_stack.append([c, 1])

        output = ""
        for c, cnt in my_stack:
            output += c * cnt
        
        return output