class Solution:
    def canPartition(self, nums):
        def dfs(ind, cur_sum):
            if ind == len(nums):
                if cur_sum == target_sum:
                    return True
                return False

            if cur_sum > target_sum:
                return False
            
            if (ind, cur_sum) in cache:
                return cache[(ind, cur_sum)]

            cache[(ind, cur_sum)] = dfs(ind + 1, cur_sum + nums[ind]) or dfs(ind + 1, cur_sum)
            return cache[(ind, cur_sum)]

        target_sum = sum(nums) // 2 
        if sum(nums) % 2 == 1:
            return False

        cache = {}
        return dfs(0, 0)
        