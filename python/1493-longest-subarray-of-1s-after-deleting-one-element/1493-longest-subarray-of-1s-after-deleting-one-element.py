class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_count = 0
        zero = 0
        start = 0

        for ind in range(len(nums)):
            if nums[ind] == 0:
                zero += 1

            if zero > 1:
                if nums[start] == 0:
                    zero -= 1
                start += 1

            max_count = max(max_count, ind - start + 1)

        return max_count - 1
