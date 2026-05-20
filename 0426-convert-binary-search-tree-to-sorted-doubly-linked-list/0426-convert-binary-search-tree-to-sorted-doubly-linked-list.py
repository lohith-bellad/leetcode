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
        def traverse(root):
            if not root:
                return root
            
            traverse(root.left)

            if self.tail:
                self.tail.right = root
                root.left = self.tail
            else:
                self.head = root

            self.tail = root

            traverse(root.right)
            return
        
        if not root:
            return root

        self.head = None
        self.tail = None
        traverse(root)

        self.head.left = self.tail
        self.tail.right = self.head

        return self.head
