"""
152. Maximum Product Subarray
Medium

Given an integer array nums, find a contiguous non-empty subarray within the array
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:
    * 1 <= nums.length <= 2 * 10^4
    * -10 <= nums[i] <= 10
    * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 1
        cur_min = 1
        max_product = int("-inf")

        for num in nums:
            temp = cur_max
            cur_max = max(num, cur_max * num, cur_min * num)
            cur_min = min(temp * num, num, num * cur_min)
            max_product = max(max_product, cur_max)

        return max_product
