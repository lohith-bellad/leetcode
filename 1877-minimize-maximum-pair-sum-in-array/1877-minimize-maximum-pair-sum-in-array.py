class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0

        start = 0
        end = len(nums) - 1

        while start < end:
            cur_pair_sum = nums[start] + nums[end]

            output = max(output, cur_pair_sum)

            start += 1
            end -= 1
        
        return output