"""
886. Possible Bipartition
Medium

We want to split a group of n people (labeled from 1 to n) into two groups of
any size. Each person may dislike some other people, and they should not go
into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
indicates that the person labeled ai does not like the person labeled bi,
return true if it is possible to split everyone into two groups in this way.


Example 1:
    Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: The first group has [1,4], and the second group has [2,3].

Example 2:
    Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false
    Explanation: We need at least 3 groups to divide them. We cannot put them
        in two groups.

Example 3:
    Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false


Constraints:
    * 1 <= n <= 2000
    * 0 <= dislikes.length <= 10^4
    * dislikes[i].length == 2
    * 1 <= ai < bi <= n
    * All the pairs of dislikes are unique.

"""

from typing import List
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, p):
            party[node] = p

            for neighbor in ntable[node]:
                if party[node] == party[neighbor]:
                    return False

                if party[neighbor] == -1:
                    if not dfs(neighbor, 1 - p):
                        return False

            return True

        party = [-1 for _ in range(n + 1)]
        ntable = defaultdict(list)

        for s, d in dislikes:
            ntable[s].append(d)
            ntable[d].append(s)

        for i in range(1, n + 1):
            if party[i] == -1 and not dfs(i, 0):
                return False

        return True
