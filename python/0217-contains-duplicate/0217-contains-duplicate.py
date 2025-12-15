class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                return True

        return False
