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

        prefix_mod = 0
        mod_map = {0: -1}

        for i in range(len(nums)):
            prefix_mod += nums[i]
            prefix_mod %= k

            if prefix_mod in mod_map:
                if i - mod_map[prefix_mod] > 1:
                    return True
            else:
                mod_map[prefix_mod] = i

        return False

        return False
