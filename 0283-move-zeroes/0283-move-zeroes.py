class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pivot = 0
        idx = 0

        while idx < len(nums):
            if nums[idx] != 0:
                nums[idx], nums[pivot] = nums[pivot], nums[idx]
                pivot += 1
            idx += 1
        
        return
