class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def traverse(ind, exp, value, last):
            if ind == len(num):
                if value == target:
                    output.append(exp)
                return
            
            for i in range(ind, len(num)):
                if i > ind and num[ind] == "0":
                    return
                
                cur = int(num[ind : i + 1])

                if ind == 0:
                    traverse(i + 1, exp + str(cur), cur, cur)
                else:
                    traverse(i + 1, exp + "+" + str(cur), value + cur, cur)
                    traverse(i + 1, exp + "-" + str(cur), value - cur, -cur)
                    traverse(i + 1, exp + "*" + str(cur), value - last + last * cur, last * cur)

        output = []
        traverse(0, "", 0, 0)
        return output