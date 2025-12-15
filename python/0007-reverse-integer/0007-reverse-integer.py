class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        res = 0

        if x < 0:
            is_negative = True
            inp = -x
        else:
            inp = x

        while inp > 0:
            temp = (res * 10) + (inp % 10)
            if temp > 2**31:
                return 0
            res = temp
            inp = inp // 10

        if is_negative:
            return -res
        else:
            return res
