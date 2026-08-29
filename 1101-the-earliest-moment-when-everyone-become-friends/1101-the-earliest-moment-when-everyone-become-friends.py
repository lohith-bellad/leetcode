class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find_parent(self, node: int):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find_parent(n1)
        p2 = self.find_parent(n2)

        if p1 == p2:
            return False

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2] + 1
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1] + 1

        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        group = {}

        for ts, a, b in logs:
            uf.union(a, b)
            root = uf.find_parent(a)
            if uf.rank[root] == n - 1:
                return ts        
        
        return -1