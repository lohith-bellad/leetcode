class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()

        while n > 1:
            total = 0

            while n > 0:
                total += (n % 10) ** 2
                n //= 10

            if total in nset:
                return False
            nset.add(total)

            n = total

        return True
