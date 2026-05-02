class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = 0
        table = {}
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            table[nums[right]] = table.get(nums[right], 0) + 1

            while left < right and table[nums[right]] > 1:
                cur_sum -= nums[left]
                table[nums[left]] -= 1
                if not table[nums[left]]:
                    del table[nums[left]]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, cur_sum)

                cur_sum -= nums[left]
                table[nums[left]] -= 1
                if table[nums[left]] == 0:
                    del table[nums[left]]
                left += 1

        return max_sum