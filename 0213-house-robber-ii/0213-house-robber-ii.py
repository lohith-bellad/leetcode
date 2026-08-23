class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        def rob_path(arr):
            t1 = 0
            t2 = 0

            for cur in arr:
                temp = t1
                t1 = max(t1, cur + t2)
                t2 = temp
            
            return t1

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(rob_path(nums[:-1]), rob_path(nums[1:]))
        """
        if len(nums) == 1:
            return nums[0]
            
        def dfs(ind, max_ind, cache):
            if ind >= max_ind:
                return 0
        
            if ind not in cache:
                taken = dfs(ind + 2, max_ind, cache) + nums[ind]
                skipped = dfs(ind + 1, max_ind, cache)
                cache[ind] = max(taken, skipped)
        
            return cache[ind]
                
        cache1 = {}
        res1 = dfs(0, len(nums) - 1, cache1)
        cache2 = {}
        res2 = dfs(1, len(nums), cache2)

        return max(res1, res2)