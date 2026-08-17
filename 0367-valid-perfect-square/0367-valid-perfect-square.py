import math 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = math.ceil(num / 2)

        while start <= end:
            mid = start + (end - start) // 2

            if mid * mid == num:
                return True
            
            if mid * mid > num:
                end = mid - 1
            else:
                start = mid + 1

        return False