class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        def traverse(ind: int) -> bool:
            if cache[ind] != -1:
                return cache[ind]

            min_jumps = float('inf')
            for i in range(ind + 1, min(len(nums) - 1, ind + nums[ind]) + 1):
                jumps = traverse(i) + 1
                min_jumps = min(min_jumps, jumps)
            
            cache[ind] = min_jumps
            return cache[ind]
        
        cache = [-1 for i in range(len(nums))]
        cache[-1] = 0
        return traverse(0)
        """
        def dfs(ind):
            if ind >= len(nums) - 1:
                return 0
            
            if ind in cache:
                return cache[ind]
            
            min_steps = float("inf")
            for jump in range(1, nums[ind] + 1):
                steps = dfs(ind + jump)
                min_steps = min(min_steps, steps)

            cache[ind] = min_steps + 1
            return cache[ind]
        
        cache = {}
        return dfs(0)