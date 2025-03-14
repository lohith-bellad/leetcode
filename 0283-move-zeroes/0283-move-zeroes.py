class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0

        for ind in range(len(nums)):
            if nums[zero_ptr] == 0 and nums[ind] != 0:
                nums[zero_ptr] = nums[ind]
                nums[ind] = 0

            if nums[zero_ptr] != 0:
                zero_ptr += 1