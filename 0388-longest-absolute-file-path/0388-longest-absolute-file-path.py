class Solution:
    def lengthLongestPath(self, input: str) -> int:
        myStack = []
        if "." not in input:
            return 0

        inps = input.split("\n")
        max_len = 0
        
        for inp in inps:
            level = inp.count("\t")
            name_len = len(inp) - level
            
            while myStack and myStack[-1][0] >= level:
                myStack.pop()
                
            if myStack:
                last = myStack[-1][1]
            else:
                last = 0
            myStack.append((level, name_len + last))
            
            if "." in inp:
                max_len = max(max_len, sum(myStack[-1]))

        return max_len