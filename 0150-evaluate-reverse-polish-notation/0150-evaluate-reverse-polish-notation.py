class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        signs = ["+", "-", "/", "*"]

        for token in tokens:
            if token not in signs:
                temp.append(int(token))
            else:
                if len(temp) >= 2:
                    num1 = temp.pop()
                    num2 = temp.pop()

                    if token == "+":
                        temp.append(num1 + num2)
                    elif token == "-":
                        temp.append(num2 - num1)
                    elif token == "*":
                        temp.append(num1 * num2)
                    else:
                        temp.append(int(num2 / num1))
            
        return temp[0]