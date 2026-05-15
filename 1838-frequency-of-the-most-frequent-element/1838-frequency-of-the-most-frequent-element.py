class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = 0
        max_freq = 0
        cur_sum = 0
        nums.sort()

        for right in range(len(nums)):
            cur_sum += nums[right]

            while left < right and (nums[right] * (right - left + 1)) - cur_sum > k:
                cur_sum -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq