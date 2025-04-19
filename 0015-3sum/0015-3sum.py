class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        left_hash = {}
        right_hash = {}
        nums.sort()
    
        left_hash[nums[0]] = 1
        for i in range(1, len(nums)):
            right_hash[nums[i]] = right_hash.get(nums[i], 0) + 1
        
        for i in range(1, len(nums)):
            right_hash[nums[i]] -= 1
            if right_hash[nums[i]] == 0:
                del right_hash[nums[i]]
            
            for key in left_hash.keys():
                search = -(key + nums[i])
                if search in right_hash:
                    output.add((key, nums[i], search))
            
            left_hash[nums[i]] = left_hash.get(nums[i], 0) + 1
    
        return list(output)


