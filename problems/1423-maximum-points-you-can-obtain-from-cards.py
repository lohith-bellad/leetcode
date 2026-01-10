"""
1423. Maximum Points You Can Obtain from cardPoints
Medium

There are several cardPoints arranged in a row, and each card has an associated number of points.
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have
to take exactly k cardPoints.

Your score is the sum of the points of the cardPoints you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can
obtain.


Example 1:
    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    Explanation: After the first step, your score will always be 1. However, choosing the
    rightmost card first will maximize your total score. The optimal strategy is to take
    the three cardPoints on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
    Input: cardPoints = [2,2,2], k = 2
    Output: 4
    Explanation: Regardless of which two cardPoints you take, your score will always be 4.

Example 3:
    Input: cardPoints = [9,7,7,9,7,7,9], k = 7
    Output: 55
    Explanation: You have to take all the cardPoints. Your score is the sum of points of all
    cardPoints.


Constraints:
    * 1 <= cardPoints.length <= 10^5
    * 1 <= cardPoints[i] <= 10^4
    * 1 <= k <= cardPoints.length

"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)

        cur_sum = 0
        max_sum = 0

        for i in range(k):
            cur_sum += cardPoints[i]

        max_sum = cur_sum

        i = k - 1
        j = len(cardPoints) - 1
        while i >= 0:
            cur_sum -= cardPoints[i]
            cur_sum += cardPoints[j]
            max_sum = max(max_sum, cur_sum)
            i -= 1
            j -= 1

        return max_sum
