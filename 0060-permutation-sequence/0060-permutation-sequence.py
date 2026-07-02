class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        output = []
        inps = [i for i in range(1, n + 1)]
        k -= 1

        for i in range(n, 0, -1):
            idx = factorial(i - 1)
            b_idx = k // idx
            k = k % idx

            output.append(str(inps.pop(b_idx)))
        
        return "".join(output)