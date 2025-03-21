class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        total_sum = 0
        cur_max = 0
        cur_min = 0

        for num in nums:
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min, 0) + num
            min_sum = min(min_sum, cur_min)

            total_sum += num
        
        if total_sum == min_sum:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)
