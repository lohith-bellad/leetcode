"""
323. Number of Connected Components in an Undirected Graph
Medium

You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
in the graph.

Return the number of connected components in the graph.


Example 1:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1


Constraints:
    * 1 <= n <= 2000
    * 1 <= edges.length <= 5000
    * edges[i].length == 2
    * 0 <= ai <= bi < n
    * ai != bi
    * There are no repeated edges.

"""

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.weight = [0 for _ in range(n)]

    def find(self, n: int) -> int:
        while self.parent[n] != n:
            n = self.parent[n]

        return n

    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
            self.weight[p1] += 1
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        output = set()

        for edge in edges:
            a, b = edge
            uf.union(a, b)

        for i in range(n):
            p = uf.find(i)
            output.add(p)

        return len(output)
