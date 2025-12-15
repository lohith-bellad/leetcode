class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        my_stack = []

        for bracket in s:
            if bracket == ")":
                if len(my_stack) > 0 and my_stack[-1] == "(":
                    my_stack.pop()
                else:
                    my_stack.append(bracket)
            else:
                my_stack.append(bracket)

        return len(my_stack)
        """
        p_stack = []
        result = 0

        for i in range(len(s)):
            if s[i] in "(":
                p_stack.append("(")
            else:
                if p_stack:
                    p_stack.pop()
                else:
                    result += 1

        result += len(p_stack)

        return result
