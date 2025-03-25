class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()

        while n > 1:
            total = 0
            num = n

            while num > 0:
                total += (num % 10)**2
                num = num // 10
            
            if total in nset:
                return False
            nset.add(total)

            n = total
        
        return True