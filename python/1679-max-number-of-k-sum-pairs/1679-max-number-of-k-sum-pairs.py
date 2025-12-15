class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0

        first = 0
        last = len(nums) - 1

        while first < last:
            s = nums[first] + nums[last]
            if s == k:
                count += 1
                first += 1
                last -= 1
            elif s > k:
                last -= 1
            elif s < k:
                first += 1

        return count
