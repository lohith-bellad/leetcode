"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
    Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9


Constraints:
    * 0 <= nums.length <= 10^5
    * -10^9 <= nums[i] <= 10^9

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        input = set(nums)

        for num in input:
            if num + 1 in input:
                continue

            count = 0
            while num in input:
                num -= 1
                count += 1
            max_count = max(max_count, count)

        return max_count
