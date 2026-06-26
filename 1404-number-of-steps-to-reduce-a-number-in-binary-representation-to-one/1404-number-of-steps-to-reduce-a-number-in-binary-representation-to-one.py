class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        s = list(s)

        while '1' in s[:len(s) - 1]:
            pivot = s[-1]
            
            #Even number
            if pivot == '0':
                num = ['0']
                num += s[:len(s) - 1]
                s = num
            # Odd Number
            else:
                s[-1] = '0'
                ind = len(s) - 2
                while ind >= 0:
                    if s[ind] == '0':
                        s[ind] = '1'
                        break
                    s[ind] = "0"
                    ind -= 1
                
                if ind == -1:
                    s = ['1'] + s

            count += 1

        return count 