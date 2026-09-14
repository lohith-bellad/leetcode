class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
            
        gcd = math.gcd(x, y)
        return target % gcd == 0