"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {}
        root = head
        dummy = Node(0)
        prev = dummy

        while root != None:
            new_node = Node(root.val)
            prev.next = new_node
            table[root] = new_node
            prev = new_node
            root = root.next
        
        old_head = head
        new_head = dummy.next

        while old_head != None:
            if old_head.random != None:
                new_head.random = table[old_head.random]
            old_head = old_head.next
            new_head = new_head.next

        return dummy.next