class Solution:
    def check(self, nums: List[int]) -> bool:
        start = -1

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                start = i + 1
                break
        
        if start == -1:
            return True
        
        for i in range(start, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        
        return nums[i + 1] <= nums[0]