class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n: int) -> int:
            if n == 0:
                return 1

            return n * fact(n - 1)

        num = fact(n)
        cnt = 0
        while num > 0:
            if num % 10 == 0:
                cnt += 1
                num = num // 10
            else:
                break

        return cnt
