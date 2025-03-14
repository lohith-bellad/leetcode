class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 1
        output = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            output[i] = temp * nums[i - 1]
            temp = output[i]
        
        idx = len(nums) - 1
        temp = nums[idx]
        for i in range(len(nums) - 2, -1, -1):
            output[i] = temp * output[i]
            temp = temp * nums[i]
        
        return output
