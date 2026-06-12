class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = nums[1:]
        n.sort()
        return nums[0] + n[0] + n[1]