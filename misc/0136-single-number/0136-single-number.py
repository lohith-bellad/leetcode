class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0

        for n in nums:
            output = output ^ n

        return output
