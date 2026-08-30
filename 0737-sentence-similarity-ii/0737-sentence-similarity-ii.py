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
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        word_idx = {}
        cur_idx = 0
        words = set()

        for a, b in similarPairs:
            words.add(a)
            words.add(b)

        uf = UnionFind(len(words))

        for a, b in similarPairs:
            if a not in word_idx:
                word_idx[a] = cur_idx
                cur_idx += 1
            if b not in word_idx:
                word_idx[b] = cur_idx
                cur_idx += 1
            uf.union(word_idx[a], word_idx[b])

        if len(sentence1) != len(sentence2):
            return False

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            
            if sentence1[i] not in word_idx or sentence2[i] not in word_idx:
                return False
                
            if uf.find_parent(word_idx[sentence1[i]]) != uf.find_parent(word_idx[sentence2[i]]):
                return False

        return True            

