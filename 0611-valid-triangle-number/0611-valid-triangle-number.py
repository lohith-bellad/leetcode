class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        nums.sort()
        count = 0
        third_ind = len(nums) - 1

        while third_ind >= 2:
            left = 0
            right = third_ind - 1

            while left < right:
                if nums[left] + nums[right] > nums[third_ind]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

            third_ind -= 1
        
        return count
        """
        nums.sort()
        count = 0

        ind = len(nums) - 1

        while ind >= 2:
            left = 0
            right = ind - 1

            while left < right:
                if nums[left] + nums[right] > nums[ind]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
            ind -= 1
        
        return count
        


