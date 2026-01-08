"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.


Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array
    [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being
    trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9


Constraints:
    * n == height.length
    * 1 <= n <= 2 * 10^4
    * 0 <= height[i] <= 10^5

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        water = 0

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])

        right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]

        return water
