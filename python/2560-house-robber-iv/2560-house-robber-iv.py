class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        start = 1
        end = max(nums)

        while start < end:
            mid = start + (end - start) // 2

            rob = 0
            ind = 0
            while ind < len(nums):
                if nums[ind] <= mid:
                    rob += 1
                    ind += 2
                else:
                    ind += 1

            if rob >= k:
                end = mid
            else:
                start = mid + 1

        return start
