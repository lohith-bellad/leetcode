class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_braces = ['(', '{', '[']

        for b in s:
            if b in open_braces:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False

                brace = stack.pop()

                if (b == ')' and brace != '(') or (b == '}' and brace != '{') or (b == ']' and brace != '['):
                    return False

        if len(stack) > 0:
            return False
            
        return True

