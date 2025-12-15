class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, n: int) -> int:
        while n != self.par[n]:
            n = self.par[n]
        return n

    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += 1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        leaders = set()

        for edge in edges:
            n1, n2 = edge
            uf.union(n1, n2)

        for i in range(n):
            l = uf.find(i)
            leaders.add(l)

        return len(leaders)
