"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(root: 'Node', pointers: ['Node'], ind: int):
            if root == None:
                return
            
            if len(pointers) == ind:
                pointers.append(root)
            else:
                pointers[ind].next = root
                pointers[ind] = root
            
            traverse(root.left, pointers, ind + 1)
            traverse(root.right, pointers, ind + 1)

            return
        
        links = []
        traverse(root, links, 0)

        for node in links:
            node.next = None
        
        return root
            
