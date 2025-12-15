class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        count = 0
        prod = 1

        if k <= 1:
            return 0

        for right in range(len(nums)):
            prod = prod * nums[right]

            while prod >= k:
                prod = prod / nums[left]
                left += 1

            count += right - left + 1

        return count
