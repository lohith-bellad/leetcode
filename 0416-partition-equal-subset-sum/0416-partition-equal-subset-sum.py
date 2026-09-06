class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        def dfs(target: int, ind: int, cache: []) -> bool:
            if target == 0:
                return True
            
            if ind == 0 or target < 0:
                return False
            
            if cache[ind][target] != -1:
                return cache[ind][target]

            cache[ind][target] = dfs(target - nums[ind], ind - 1, cache) or dfs(target, ind - 1, cache)
            return cache[ind][target]

        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target = total_sum // 2
        cache = [[-1] * (target + 1) for i in range(len(nums)+1)]

        res =  dfs(target, len(nums) - 1, cache)
        return res
        """
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
        