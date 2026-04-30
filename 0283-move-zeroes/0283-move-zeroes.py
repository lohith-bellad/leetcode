class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        pivot = 0
        idx = 0

        while idx < len(nums):
            if nums[idx] != 0:
                nums[idx], nums[pivot] = nums[pivot], nums[idx]
                pivot += 1
            idx += 1
        
        return
        '''
        pivot = 0
        ind = 0

        while ind < len(nums):
            if nums[ind] != 0:
                nums[pivot] = nums[ind]
                pivot += 1
            ind += 1
        
        while pivot < len(nums):
            nums[pivot] = 0
            pivot += 1
        
        return
