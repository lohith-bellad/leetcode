class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        zero = 0
        start = 0

        for ind in range(len(nums)):
            if nums[ind] == 0:
                zero += 1

            if zero > k:
                if nums[start] == 0:
                    zero -= 1
                start += 1

            max_length = max(max_length, ind - start + 1)

        return max_length
