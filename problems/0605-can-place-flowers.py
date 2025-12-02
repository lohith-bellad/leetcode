"""
605. Can Place Flowers
Easy

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1
means not empty, and an integer n, return true if n new flowers can be planted in
the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false


Constraints:
    * 1 <= flowerbed.length <= 2 * 10^4
    * flowerbed[i] is 0 or 1
    * There are no two adjacent flowers in flowerbed
    * 0 <= n <= flowerbed.length

"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def can_place(i: int) -> bool:
            if (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            ):
                return True
            else:
                return False

        ind = 0
        while ind < len(flowerbed) and n > 0:
            if flowerbed[ind] == 0 and can_place(ind):
                ind += 2
                n -= 1
            else:
                ind += 1

        return n == 0
