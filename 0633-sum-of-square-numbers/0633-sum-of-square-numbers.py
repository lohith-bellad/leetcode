class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        max_num = int(c**0.5)
        if max_num**2 == c:
            return True

        left = 1
        right = max_num

        while left <= right:
            cur_sum = left**2 + right**2
            if cur_sum == c:
                return True
            
            if cur_sum > c:
                right -= 1
            else:
                left += 1
        
        return False
        """
        start = 0
        end = int(c**0.5)

        while start <= end:
            if start**2 + end**2 == c:
                return True
            
            if start**2 + end**2 < c:
                start += 1
            else:
                end -= 1
        
        return False
            
            