"""
611. Valid Triangle Number
Medium

Given an integer array nums, return the number of triplets chosen from the
array that can make triangles if we take them as side lengths of a triangle.


Example 1:
    Input: nums = [2,2,3,4]
    Output: 3
    Explanation: Valid combinations are:
        2,3,4 (using the first 2)
        2,3,4 (using the second 2)
        2,2,3

Example 2:
    Input: nums = [4,2,3,4]
    Output: 4


Constraints:
    * 1 <= nums.length <= 1000
    * 0 <= nums[i] <= 1000

"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output = 0

        max_side = len(nums) - 1
        
        while max_side >= 2:
            left = 0
            right = max_side - 1

            while left < right:
                if nums[left] + nums[right] > nums[max_side]:
                    output += right - left
                    right -= 1
                else:
                    left += 1

            max_side -= 1

        return output




