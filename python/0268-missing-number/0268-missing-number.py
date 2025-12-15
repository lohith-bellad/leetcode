class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        given_total = sum(nums)
        n = len(nums)
        actual_total = (n * (n + 1)) // 2

        return actual_total - given_total
