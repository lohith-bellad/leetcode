class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s
    
        pstack = []
        s_list = list(s)
        output = []

        ind = 0
        for c in s_list:
            if c == "(":
                pstack.append(ind)
                output.append(c)
                ind += 1
            elif c == ")":
                if pstack:
                    pstack.pop()
                    output.append(c)
                    ind += 1
            else:
                output.append(c)
                ind += 1
    
        for ind in pstack:
            output[ind] = ""
    
        return "".join(output)
        
    