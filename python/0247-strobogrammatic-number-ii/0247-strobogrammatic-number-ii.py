class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        mapping = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

        def traverse(ind: int) -> []:
            if ind == 0:
                return [""]
            if ind == 1:
                return ["0", "1", "8"]
            else:
                res = traverse(ind - 2)
            
            num = []

            for r in res:
                for k, v in mapping.items():
                    if ind == n and k == "0":
                        continue
                    num.append(k + r + v)
            
            return num
        
        return traverse(n)