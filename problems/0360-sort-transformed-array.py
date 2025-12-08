"""
360. Sort Transformed Array
Medium

Given a sorted integer array nums and three integers a, b and c, apply a quadratic
function of the form f(x) = ax^2 + bx + c to each element nums[i] in the array, and
return the array in a sorted order.


Example 1:
    Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
    Output: [3,9,15,33]
    Explanation:
        f(-4) = 1*(-4)^2 + 3*(-4) + 5 = 16 - 12 + 5 = 9
        f(-2) = 1*(-2)^2 + 3*(-2) + 5 = 4 - 6 + 5 = 3
        f(2) = 1*(2)^2 + 3*(2) + 5 = 4 + 6 + 5 = 15
        f(4) = 1*(4)^2 + 3*(4) + 5 = 16 + 12 + 5 = 33
        Sorted: [3,9,15,33]

Example 2:
    Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
    Output: [-23,-5,1,7]
    Explanation:
        f(-4) = -1*(-4)^2 + 3*(-4) + 5 = -16 - 12 + 5 = -23
        f(-2) = -1*(-2)^2 + 3*(-2) + 5 = -4 - 6 + 5 = -5
        f(2) = -1*(2)^2 + 3*(2) + 5 = -4 + 6 + 5 = 7
        f(4) = -1*(4)^2 + 3*(4) + 5 = -16 + 12 + 5 = 1
        Sorted: [-23,-5,1,7]


Constraints:
    * 1 <= nums.length <= 200
    * -100 <= nums[i], a, b, c <= 100
    * nums is sorted in ascending order.


Follow up: Could you solve it in O(n) time?

"""


class Solution:
    def sortTransformedArray(
        self, nums: List[int], a: int, b: int, c: int
    ) -> List[int]:
        def evaluate(num):
            return (a * num**2) + (b * num) + c

        left = 0
        right = len(nums) - 1
        output = []

        if a < 0:
            while left <= right:
                left_y = evaluate(nums[left])
                right_y = evaluate(nums[right])

                if left_y < right_y:
                    output.append(left_y)
                    left += 1
                else:
                    output.append(right_y)
                    right -= 1
        else:
            while left <= right:
                left_y = evaluate(nums[left])
                right_y = evaluate(nums[right])

                if left_y > right_y:
                    output.append(left_y)
                    left += 1
                else:
                    output.append(right_y)
                    right -= 1

            output.reverse()
        return output
