class Solution:
    def calculate(self, s: str) -> int:
        """
        s = "(" + s + ")"
        my_stack = []
        sign_stack = []

        idx = 0
        op = "+"
        while idx < len(s):
            while s[idx] == " ":
                idx += 1

            num = 0
            while idx < len(s) and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1

            if num > 0:
                if op == "+":
                    my_stack.append(num)
                elif op == "-":
                    my_stack.append(-num)

            if s[idx] in "+-":
                op = s[idx]

            if s[idx] == "(":
                sign_stack.append(op)
                op = "+"
                my_stack.append("(")

            if s[idx] == ")":
                temp = []
                while my_stack and my_stack[-1] != "(":
                    temp.append(my_stack.pop())
                my_stack.pop()
                new_num = sum(temp)
                last_op = sign_stack.pop()
                if last_op == "-":
                    my_stack.append(-new_num)
                else:
                    my_stack.append(new_num)

            idx += 1

        return my_stack[0]
        """
        s = "(" + s + ")"
        num_stack = []
        ind = 0
        op_stack = []
        op = "+"

        while ind < len(s):
            if s[ind] == "(":
                num_stack.append("(")
                op_stack.append(op)
                op = "+"
            elif s[ind] in "+-":
                if s[ind] == "-":
                    op = "-"
                else:
                    op = "+"
            elif s[ind].isdigit():
                num = 0
                while ind < len(s) and s[ind].isdigit():
                    num = num * 10 + int(s[ind])
                    ind += 1
                
                if num > 0:
                    if op == "-":
                        num = -num
                    num_stack.append(str(num))
                continue
            elif s[ind] == ")":
                cur_result = 0
                while num_stack and num_stack[-1] != "(":
                    cur_result += int(num_stack.pop())
                num_stack.pop()
                cur_op = op_stack.pop()
                if cur_op == "-":
                    cur_result = -cur_result
                num_stack.append(str(cur_result))
            
            ind += 1
        
        return int(num_stack[0])
