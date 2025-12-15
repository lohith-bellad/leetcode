"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees
of every node never differs by more than one.


Example 1:
    Input: root = [3,9,20,null,null,15,7]
          3
         / \
        9  20
          /  \
         15   7
    Output: true

Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
            1
           / \
          2   2
         / \
        3   3
       / \
      4   4
    Output: false

Example 3:
    Input: root = []
    Output: true


Constraints:
    * The number of nodes in the tree is in the range [0, 5000].
    * -10^4 <= Node.val <= 10^4

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return 0, True

            left_depth, left_balanced = traverse(root.left)
            right_depth, right_balanced = traverse(root.right)

            if not left_balanced or not right_balanced:
                return -1, False

            if abs(left_depth - right_depth) > 1:
                return -1, False

            return max(left_depth, right_depth) + 1, True

        _, is_balanced = traverse(root)
        return is_balanced
