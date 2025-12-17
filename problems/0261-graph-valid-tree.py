"""
261. Graph Valid Tree
Medium

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list
of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes
ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.


Example 1:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false


Constraints:
    * 1 <= n <= 2000
    * 0 <= edges.length <= 5000
    * edges[i].length == 2
    * 0 <= ai, bi < n
    * ai != bi
    * There are no self-loops or repeated edges.

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for edge in edges:
            a, b = edge

            if not uf.union(a, b):
                return False
        
        output = set()
        for i in range(n):
            p = uf.find(i)
            output.add(p)

        return len(output) == 1
