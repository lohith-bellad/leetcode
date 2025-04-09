class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = [0 for i in range(101)]

        for num in nums:
            counts[num] += 1
        
        start = 0
        end = len(nums) - 1
        cnt = 0
        while start < len(nums) and max(counts) > 1:
            cnt += 1
            end = min(start + 3, len(nums) - 1)
            for i in range(start, end):
                counts[nums[i]] -= 1
            start = start + 3
        
        return cnt