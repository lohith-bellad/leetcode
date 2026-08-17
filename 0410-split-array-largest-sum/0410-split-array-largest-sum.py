class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split_k(num):
            count = 1
            cur_sum = 0
            idx = 0

            while idx < len(nums):
                if cur_sum + nums[idx] <= num:
                    cur_sum += nums[idx]
                else:
                    cur_sum = nums[idx]
                    count += 1
                idx += 1
            
            return count <= k

        start = max(nums)
        end = sum(nums)

        while start < end:
            mid = start + (end - start) // 2

            if can_split_k(mid):
                end = mid
            else:
                start = mid + 1
        
        return start