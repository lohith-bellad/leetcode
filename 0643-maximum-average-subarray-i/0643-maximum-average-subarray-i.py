class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = float("-inf")
        ans = 0

        for n in range(k):
            ans = ans + nums[n]
        avg = max(avg, ans / k)

        j = k
        i = 0
        while j < len(nums):
            ans = ans - nums[i]
            ans = ans + nums[j]

            avg = max(avg, ans / k)

            j += 1
            i += 1
        
        return avg