class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashset = set()
        output = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    pivot = target - nums[i] - nums[j] - nums[k]
                    if pivot in hashset:
                        output.add(tuple(sorted([nums[i], nums[j], nums[k], pivot])))
            hashset.add(nums[i])
        
        return list(output)