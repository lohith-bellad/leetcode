"""
698. Partition to K Equal Sum Subsets
Medium

Given an integer array nums and an integer k, return true if it is possible to divide
this array into k non-empty subsets whose sums are all equal.


Example 1:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2, 3), (2, 3)
                 with equal sums.

Example 2:
    Input: nums = [1,2,3,4], k = 3
    Output: false


Constraints:
    * 1 <= k <= nums.length <= 16
    * 1 <= nums[i] <= 10^4
    * The frequency of each element is in the range [1, 4].

"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(ind, cur_sum, count):
            nonlocal mask
            if count == k - 1:
                return True

            if cur_sum > sub_sum:
                return False

            if mask in memo:
                return memo[mask]

            if cur_sum == sub_sum:
                memo[mask] = backtrack(0, 0, count + 1)
                return memo[mask]

            for i in range(ind, len(nums)):
                if (mask & (1 << i)) == 0:
                    mask |= 1 << i

                    if backtrack(i + 1, cur_sum + nums[i], count):
                        return True

                    mask ^= 1 << i

            return False

        total_sum = sum(nums)

        if total_sum % k != 0:
            return False

        sub_sum = total_sum // k
        nums.sort(reverse=True)

        mask = 0
        memo = {}

        return backtrack(0, 0, 0)
