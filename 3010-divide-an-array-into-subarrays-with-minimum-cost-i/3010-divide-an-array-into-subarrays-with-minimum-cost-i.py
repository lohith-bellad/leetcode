class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        output = nums[0]

        mins = [float("inf"), float("inf")]
        for i in range(1, len(nums)):
            if nums[i] < mins[0]:
                mins[1] = mins[0]
                mins[0] = nums[i]
            elif nums[i] < mins[1]:
                mins[1] = nums[i]
        
        return output + sum(mins)