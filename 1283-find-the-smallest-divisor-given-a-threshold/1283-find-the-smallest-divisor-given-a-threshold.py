class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def can_divide(d):
            cur_sum = 0

            for n in nums:
                cur_sum += math.ceil(n / d)
            
            return cur_sum <= threshold

        start = 1
        end = max(nums)

        while start < end:
            mid = start + (end - start) // 2

            if can_divide(mid):
                end = mid
            else:
                start = mid + 1
        
        return start