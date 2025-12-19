"""
633. Sum of Square Numbers
Medium

Given a non-negative integer c, decide whether there are two integers a and b
such that a^2 + b^2 = c.


Example 1:
    Input: c = 5
    Output: true
    Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
    Input: c = 3
    Output: false


Constraints:
    * 0 <= c <= 2^31 - 1

"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_num = int(c**0.5)
        if max_num**2 == c:
            return True

        left = 1
        right = max_num

        while left <= right:
            cur_sum = left**2 + right**2
            if cur_sum == c:
                return True

            if cur_sum > c:
                right -= 1
            else:
                left += 1

        return False
