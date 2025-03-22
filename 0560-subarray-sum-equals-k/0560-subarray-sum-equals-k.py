class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {0 : 1}
        total = 0
        count = 0

        for i in range(len(nums)):
            total += nums[i]
            search = total - k

            if search in hash_table:
                count += hash_table[search]
            
            if total not in hash_table:
                hash_table[total] = 0
            hash_table[total] += 1
        
        return count