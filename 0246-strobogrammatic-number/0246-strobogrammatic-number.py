class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        inp = list(num)
        comp = list(num)
        comp.reverse()

        for a, b in zip(inp, comp):
            if a not in mapping or mapping[a] != b:
                return False
            
        return True