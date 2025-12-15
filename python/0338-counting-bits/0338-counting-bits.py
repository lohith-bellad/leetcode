class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def count(n: int) -> int:
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count

        for i in range(n + 1):
            output.append(count(i))

        return output
