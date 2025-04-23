class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def traverse(nums: List[int], ind: int) -> [[]]:
            if ind == len(nums):
                return [[]]
            
            temp = []
            thash = {}
            perms = traverse(nums, ind + 1)
            for perm in perms:
                for j in range(len(perm) + 1):
                    pc = perm.copy()
                    pc.insert(j, nums[ind])
                    key = ','.join(map(str, pc))
                    if key not in thash:
                        temp.append(pc)
                        thash[key] = 1
            return list(temp)
        
        return traverse(nums, 0)