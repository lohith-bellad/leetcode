class Solution:
 
    def canJump(self, nums: List[int]) -> bool:
        """
        def traverse(ind: int) -> bool:
            if cache[ind] != -1:
                return cache[ind] == 1
            
            if nums[ind] == 0:
                return False

            for i in range(ind + 1, min(len(nums) - 1, ind + nums[ind]) + 1):
                if traverse(i) == True:
                    cache[ind] = 1
                    return True
            
            cache[ind] = 0
            return False
        
        cache = [-1 for i in range(len(nums))]
        cache[-1] = 1
        return traverse(0)
        """
        last_pos = len(nums) - 1
    
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
    
        return last_pos == 0
