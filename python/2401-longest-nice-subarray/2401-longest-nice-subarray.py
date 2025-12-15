class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1

        left = 0
        right = 1
        max_size = 1

        while right < len(nums):
            i = left
            while i < right:
                if nums[i] & nums[right] != 0:
                    break
                else:
                    i += 1
            max_size = max(max_size, i - left + 1)
            if i == right:
                right += 1
            else:
                left = i + 1
                right = left + 1

        return max_size
