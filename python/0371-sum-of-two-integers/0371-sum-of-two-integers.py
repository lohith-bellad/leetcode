class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0 
        carry = 0
        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            res = a ^ b
            carry = a & b
            a = res
            b = carry << 1
        
        if b > 0:
            return a & mask
        else:
            return a
