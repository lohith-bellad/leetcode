class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        cur_product = 1
        count = 0

        for right in range(len(nums)):
            cur_product *= nums[right]

            while cur_product >= k:
                cur_product //= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count