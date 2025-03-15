class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        table = set()

        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1
    
            max_len = max(max_len, count)
        
        return max_len