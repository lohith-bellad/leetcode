"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.head = None
        self.tail = None

        def traverse(root: 'Node'):
            if root == None:
                return
            
            traverse(root.left)

            if self.tail != None:
                self.tail.right = root
                root.left = self.tail
            else:
                self.head = root

            self.tail = root

            traverse(root.right)
            return
        
        if root == None:
            return None
            
        traverse(root)
        self.tail.right = self.head
        self.head.left = self.tail

        return self.head
