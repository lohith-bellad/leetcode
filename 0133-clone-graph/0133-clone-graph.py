"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        mapping = {}
        neighbor_list = {}
        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            n = queue.popleft()

            new_node = Node(n.val)
            mapping[n.val] = new_node
            neighbor_list[n.val] = []
            
            for neighbor in n.neighbors:
                if neighbor.val not in mapping:
                    queue.append(neighbor)
                
                neighbor_list[n.val].append(neighbor.val)

        for key, val in mapping.items():
            neighbors = neighbor_list[key]

            for n in neighbors:
                val.neighbors.append(mapping[n])
        
        return mapping[1]