"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        cur_node = leaf
        prev = None

        while cur_node != root:
            if cur_node.left:
                cur_node.right = cur_node.left
            
            cur_parent = cur_node.parent
            cur_node.left = cur_parent
            if cur_parent.left == cur_node:
                cur_parent.left = None
            else:
                cur_parent.right = None

            cur_node.parent = prev
            prev = cur_node
            cur_node = cur_parent

        root.parent = prev
        return leaf