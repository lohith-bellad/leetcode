"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        def find_root(node):
            if node in cache:
                return cache[node]
            
            if node not in parent:
                return node

            cache[node] = find_root(parent[node])
            return cache[node]

        parent = {}

        for node in tree:
            for child in node.children:
                parent[child] = node
        
        cache = {}
        count = {}
        for node in tree:
           p = find_root(node)
           count[p] = count.get(p, 0) + 1

        if len(count) == 1 and max(count.values()) == len(tree):
            return next(iter(count.keys()))

        return None       

