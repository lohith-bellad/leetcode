class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traverse(nums: List[int], ind: int) -> [[]]:
            if ind == len(nums):
                return [[]]
            
            temp = []
            perms = traverse(nums, ind + 1)
            for perm in perms:
                for j in range(len(perm) + 1):
                    pc = perm.copy()
                    pc.insert(j, nums[ind])
                    temp.append(pc)
            return temp
        
        return traverse(nums, 0)