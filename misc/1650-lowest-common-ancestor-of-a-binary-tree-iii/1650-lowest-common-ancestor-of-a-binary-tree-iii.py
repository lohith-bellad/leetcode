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
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        seen = []

        while p != None:
            seen.append(p)
            p = p.parent

        while q != None:
            if q in seen:
                return q
            q = q.parent
