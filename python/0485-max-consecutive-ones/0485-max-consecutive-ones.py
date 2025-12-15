class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count = 0

        return max_count
