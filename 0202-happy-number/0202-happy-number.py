class Solution:
    def isHappy(self, n: int) -> bool:
        nset = set()

        while n > 1:
            if n in nset:
                return False
            
            nset.add(n)
            
            num = 0
            while n > 0:
                num += (n % 10)**2
                n = n // 10
        
            n = num

        return True