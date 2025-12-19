"""
2431. Maximize Total Tastiness of Purchased Fruits
Medium

You are given two non-negative integer arrays price and tastiness, both arrays
have the same length n. You are also given two non-negative integers maxAmount
and maxCoupons.

For every integer i in range [0, n - 1]:
    * price[i] describes the price of the ith fruit.
    * tastiness[i] describes the tastiness of the ith fruit.

You want to purchase some fruits such that the total tastiness is maximized
and the total price does not exceed maxAmount.

Additionally, you can use a coupon to purchase a fruit for half of its price
(rounded down to the closest integer). You can use at most maxCoupons of such
coupons.

Return the maximum total tastiness that can be purchased.

Note: You can purchase each fruit at most once. You can use coupons on some
fruit at most once.


Example 1:
    Input: price = [10,20,20], tastiness = [5,8,8], maxAmount = 20, maxCoupons = 1
    Output: 13
    Explanation: It is possible to make total tastiness 13 in following way:
        - Buy first fruit without coupon, total price = 10, tastiness = 5
        - Buy second fruit with coupon, total price = 10 + 10 = 20, tastiness = 5 + 8 = 13
        - Do not buy third fruit
        It can be proven that 13 is the maximum total tastiness that can be obtained.

Example 2:
    Input: price = [10,15,7], tastiness = [5,8,20], maxAmount = 10, maxCoupons = 2
    Output: 28
    Explanation: It is possible to make total tastiness 28 in following way:
        - Do not buy first fruit
        - Buy second fruit with coupon, total price = 7, tastiness = 8
        - Buy third fruit with coupon, total price = 7 + 3 = 10, tastiness = 8 + 20 = 28
        It can be proven that 28 is the maximum total tastiness that can be obtained.


Constraints:
    * n == price.length == tastiness.length
    * 1 <= n <= 100
    * 0 <= price[i], tastiness[i], maxAmount <= 1000
    * 0 <= maxCoupons <= 5

"""

from typing import List


class Solution:
    def maxTastiness(
        self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int
    ) -> int:
        def dfs(ind, cur_amount, cur_coupons):
            if ind >= len(price):
                return 0

            if (ind, cur_amount, cur_coupons) in cache:
                return cache[(ind, cur_amount, cur_coupons)]

            op1 = op2 = op3 = 0
            # Option-1: Do not buy current fruit
            op1 = dfs(ind + 1, cur_amount, cur_coupons)

            # Option-2: Buy without coupon
            if cur_amount + price[ind] <= maxAmount:
                op2 = tastiness[ind] + dfs(
                    ind + 1, cur_amount + price[ind], cur_coupons
                )

            # Option-3: Buy with coupon
            if (cur_amount + price[ind] // 2 <= maxAmount) and cur_coupons < maxCoupons:
                op3 = tastiness[ind] + dfs(
                    ind + 1, cur_amount + price[ind] // 2, cur_coupons + 1
                )

            cache[(ind, cur_amount, cur_coupons)] = max(op1, op2, op3)
            return cache[(ind, cur_amount, cur_coupons)]

        cache = {}
        return dfs(0, 0, 0)
