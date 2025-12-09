"""
254. Factor Combinations
Medium

Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.

Given an integer n, return all possible combinations of its factors. You may return
the answer in any order.

Note that the factors should be in the range [2, n - 1].


Example 1:
    Input: n = 1
    Output: []

Example 2:
    Input: n = 12
    Output: [[2,6],[3,4],[2,2,3]]

Example 3:
    Input: n = 37
    Output: []

Example 4:
    Input: n = 32
    Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]


Constraints:
    * 1 <= n <= 10^7

"""

from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(num, start, cur_set):
            # If num > 1 and >= start, add it as the final factor
            if num > 1 and num >= start:
                self.output.append(cur_set + [num])

            # Try all factors from start to sqrt(num)
            for i in range(start, int(num**0.5) + 1):
                if num % i == 0:
                    cur_set.append(i)
                    dfs(num // i, i, cur_set)
                    cur_set.pop()

        self.output = []
        dfs(n, 2, [])

        return self.output[1:]
