class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        nodes = [0 for i in range(n + 1)]

        for q in queries:
            nodes[q] ^= 1
        
        stack = [(1, 0)]
        while stack:
            node, val = stack.pop()

            if node > n:
                continue
            
            nodes[node] ^= val
            stack.append((node * 2, nodes[node]))
            stack.append((node * 2 + 1, nodes[node]))
        
        return sum(nodes)