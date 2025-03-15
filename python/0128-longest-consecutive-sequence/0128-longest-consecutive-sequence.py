class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        table = set(nums)

        for num in table:
            if num - 1 not in table:
                cnt = 1
                temp = num
                while temp + 1 in table:
                    cnt += 1
                    temp = temp + 1
                
                max_len = max(max_len, cnt)
        
        return max_len