class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        ind = 0
        inc = -1

        while ind < len(nums) - 1:
            if nums[ind] < nums[ind + 1]:
                if inc == -1:
                    inc = 0
                elif inc == 1:
                    return False
            elif nums[ind] > nums[ind + 1]:
                if inc == -1:
                    inc = 1
                elif inc == 0:
                    return False
            else:
                ind += 1
                continue
            ind += 1
        
        return True