class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(goal):
            if goal < 0:
                return 0
            left = 0
            count = 0
            cur_sum = 0

            for right in range(len(nums)):
                cur_sum += nums[right]

                while cur_sum > goal:
                    cur_sum -= nums[left]
                    left += 1
                
                count += right - left + 1
            
            return count

        return at_most(goal) - at_most(goal - 1)