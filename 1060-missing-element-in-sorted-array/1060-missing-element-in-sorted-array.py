class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        idx = 0
        diff = 0

        while idx < len(nums) - 1:
            diff = nums[idx + 1] - nums[idx]
            if k < diff:
                break
            idx += 1
            k -= (diff - 1)
        
        return nums[idx] + k