class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = -1
        last_min_ind = -1
        last_max_ind = -1
        count = 0

        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right
            if nums[right] == minK:
                last_min_ind = right
            if nums[right] == maxK:
                last_max_ind = right

            count += max(0, min(last_min_ind, last_max_ind) - left)
        
        return count