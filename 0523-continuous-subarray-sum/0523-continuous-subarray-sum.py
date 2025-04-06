class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        if len(nums) < 2:
            return False

        if sum(nums) % k == 0:
            return True
        
        size = 2
        while size < len(nums):
            end = size
            start = 0
            arr_sum = sum(nums[:size])

            if arr_sum % k == 0:
                return True

            while end < len(nums):
                arr_sum = arr_sum - nums[start] + nums[end]

                if arr_sum % k == 0:
                    return True
            
                start += 1
                end += 1
            size += 1
        
        return False
        """

        if len(nums) < 2:
            return False

        prefix_sum = []
        for i in range(len(nums)):
            psum = sum(nums[:i + 1])
            if psum % k == 0 and i >= 1:
                return True
            prefix_sum.append(psum)
        
        for i in range(len(nums) - 1):
            for j in range(i + 2, len(nums)):
                asum = prefix_sum[j] - prefix_sum[i]
                if asum % k == 0:
                    return True
        
        return False

        
