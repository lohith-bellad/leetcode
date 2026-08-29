class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find_parent(self, node: int):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find_parent(n1)
        p2 = self.find_parent(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        for a, b in pairs:
            uf.union(a, b)

        groups = defaultdict(list)

        for i in range(n):
            groups[uf.find_parent(i)].append(i)

        output = ["" for i in range(n)]

        for group in groups.values():
            for i, ch in zip(group, sorted(s[i] for i in group)):
                output[i] = ch

        return "".join(output)