# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.size = 0

        def traverse(root) -> int:
            if root == None:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            self.size = max(self.size, left + right)

            return max(left, right) + 1

        traverse(root)
        return self.size
