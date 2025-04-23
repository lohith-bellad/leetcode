class unionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, n: int) -> int:
        while n != self.parent[n]:
            n = self.parent[n]
        
        return n
    
    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if n1 == 2 and n2 == 5:
            print(n1, p1, n2, p2)
        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = unionFind(n)

        for n1, n2 in edges:
            if uf.union(n1, n2) == False:
                return False
        
        leader = -1
        for i in range(n):
            l = uf.find(i)
            print(l)
            if leader == -1:
                leader = l
            elif l != leader:
                return False    
        
        return True
