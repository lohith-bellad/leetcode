class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            elif abs(hash_map[nums[i]] - i) <= k:
                return True
            else:
                hash_map[nums[i]] = i

        return False
       

