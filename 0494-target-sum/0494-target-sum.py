class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(ind, path_sum):
            if ind == len(nums):
                if path_sum == target:
                    return 1
                return 0
            
            if (ind, path_sum) in cache:
                return cache[(ind, path_sum)]

            cache[(ind, path_sum)] = dfs(ind + 1, path_sum + nums[ind]) + dfs(ind + 1, path_sum - nums[ind])
        
            return cache[(ind, path_sum)]
            
        cache = {}
        return dfs(0, 0)