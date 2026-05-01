class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ind = 0

        while ind < len(nums):
            pivot = nums[ind]

            if 1 <= pivot <= len(nums) and nums[pivot - 1] != pivot:
                nums[ind], nums[pivot - 1] = nums[pivot - 1], nums[ind]
            else:
                ind += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1