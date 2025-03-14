class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = {}

        for c in s:
            if c not in table:
                table[c] = 0
            table[c] += 1

        for c in t:
            if c in table:
                table[c] -= 1
                if table[c] == 0:
                    del table[c]
            else:
                table[c] = 1
            
        for k, v in table.items():
            return k
        
        return ''
        