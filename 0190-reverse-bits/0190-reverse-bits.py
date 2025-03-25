class Solution:
    def reverseBits(self, n: int) -> int:
        inp = n & 0xFFFFFFFF
        output = []
        flag = 1

        while inp > 0:
            if flag & inp:
                output.append("1")
            else:
                output.append("0")
            inp = inp >> 1
        
        while len(output) < 32:
            output.append("0")

        return int("".join(output), 2)
