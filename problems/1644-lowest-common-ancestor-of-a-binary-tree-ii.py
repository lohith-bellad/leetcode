"""
1644. Lowest Common Ancestor of a Binary Tree II
Medium

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes,
p and q. If either node p or q does not exist in the tree, return null. The LCA is defined
as the lowest node that has both p and q as descendants (where a node can be a descendant
of itself).


Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself
                 according to the definition of LCA.

Example 3:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
    Output: null
    Explanation: Node 10 does not exist in the tree, so return null.


Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * -10^9 <= Node.val <= 10^9
    * All Node.val are unique.
    * p != q

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        def present(root, p):
            if not root:
                return False

            if root == p:
                return True

            return present(root.left, p) or present(root.right, p)

        def traverse(root, p, q):
            if not root or root == p or root == q:
                return root

            left = traverse(root.left, p, q)
            right = traverse(root.right, p, q)

            if left and right:
                return root

            if left:
                return left
            if right:
                return right

            return None

        if not present(root, p) or not present(root, q):
            return None

        return traverse(root, p, q)
        """

        def traverse(root, p, q):
            if not root:
                return None, 0

            left, lc = traverse(root.left, p, q)
            right, rc = traverse(root.right, p, q)

            if root == p or root == q:
                return root, lc + rc + 1

            if lc and rc:
                return root, lc + rc

            if left:
                return left, lc

            if right:
                return right, rc

        node, count = traverse(root, p, q)
        if count == 2:
            return node
        return None
