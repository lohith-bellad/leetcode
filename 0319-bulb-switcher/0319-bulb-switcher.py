class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 1
        count = 0
        while i <= n**0.5:
            if i * i <= n:
                count += 1
            i += 1
        
        return count

