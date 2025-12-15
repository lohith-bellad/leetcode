class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        alpha_stack = []

        i = 0
        while i < len(s):
            num = 0
            if s[i].isnumeric():
                while i < len(s) and s[i].isnumeric():
                    num = (num * 10) + int(s[i])
                    i += 1
                num_stack.append(num)
                continue

            elif s[i] == "[":
                alpha_stack.append("[")

            elif s[i] == "]":
                word = ""
                while len(alpha_stack) > 0 and alpha_stack[-1] != "[":
                    word = word + alpha_stack.pop()[::-1]

                alpha_stack.pop()
                word = word[::-1]
                cnt = num_stack.pop()
                for j in range(cnt):
                    alpha_stack.append(word)

            else:
                alpha_stack.append(s[i])

            i += 1

        return "".join(alpha_stack)
