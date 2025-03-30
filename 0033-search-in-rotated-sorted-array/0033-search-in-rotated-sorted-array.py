class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_elem = min(nums)

        for i in range(len(nums)):
            if nums[i] == start_elem:
                break
        
        offset = i

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            act_mid = (mid + offset) % len(nums)

            if nums[act_mid] == target:
                return act_mid
            
            if nums[act_mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1