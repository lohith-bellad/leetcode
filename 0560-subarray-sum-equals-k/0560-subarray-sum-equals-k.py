class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_table = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k

            if target in count_table:
                result += count_table[target]
            
            count_table[prefix_sum] = count_table.get(prefix_sum, 0) + 1

        return result 
