class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for ind, num in enumerate(nums):
            pivot = target - num
            if pivot in hash_map:
                return [hash_map[pivot], ind]
            else:
                hash_map[num] = ind
    
        return []