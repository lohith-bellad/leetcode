class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, n: int):
        while self.par[n] != n:
            n = self.par[n]
        return n
    
    def union(self, n1: int, n2: int) -> bool:
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = {}
        uf = UnionFind(len(accounts))

        for i, account in enumerate(accounts):
            for e in account[1:]:
                if e in email_to_idx:
                    uf.union(email_to_idx[e], i)
                else:
                    email_to_idx[e] = i
        
        email_group = defaultdict(list)
        for key, val in email_to_idx.items():
            root = uf.find(val)
            email_group[root].append(key)
        
        output = []
        for idx, emails in email_group.items():
            name = accounts[idx][0]
            output.append([name] + sorted(emails))

        return output