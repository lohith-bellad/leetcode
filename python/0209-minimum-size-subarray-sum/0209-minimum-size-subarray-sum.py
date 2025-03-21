class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        arr_sum = 0
        size = float('inf')

        while right < len(nums):
            arr_sum += nums[right]

            while arr_sum >= target:
                size = min(size, right - left + 1)
                arr_sum -= nums[left]
                left += 1
            right += 1
        
        if size == float('inf'):
            return 0

        return size