class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inc = 1
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            digit = inc + carry + digits[i]
            inc = 0
            if digit > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digit
                carry = 0

        out = []
        if carry == 1:
            out.append(1)

        for i in range(len(digits)):
            out.append(digits[i])

        return out
