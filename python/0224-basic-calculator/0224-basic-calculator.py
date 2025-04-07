class Solution:
    def calculate(self, s: str) -> int:
        def calculate(nums: []) -> int:
            op = "+"
            num = 0

            print(nums)
            while len(nums) > 0:
                elem = nums.pop()
                if elem.isdigit() or len(elem) > 1:
                    if op == "+":
                        num += int(elem)
                    else:
                        num -= int(elem)
                else:
                    op = elem
            
            return num

        s = "(" + s + ")"
        my_stack = []

        ind = 0
        while ind < len(s):
            while s[ind] == " ":
                ind += 1
            
            n = 0
            while s[ind].isdigit():
                n = (n * 10) + int(s[ind])
                ind += 1
            if n > 0:
                my_stack.append(str(n))

            if s[ind] == "(":
                my_stack.append(s[ind])
            elif s[ind] == ")":
                temp = []
                while my_stack[-1] != "(":
                    temp.append(my_stack.pop())
                my_stack.pop()
                my_stack.append(str(calculate(temp)))
            else:
                my_stack.append(s[ind])
            ind += 1
        
        return int(my_stack[0])

