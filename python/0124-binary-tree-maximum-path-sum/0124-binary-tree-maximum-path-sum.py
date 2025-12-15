# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def traverse(root):
            if root is None:
                return 0

            left_arm = max(0, traverse(root.left))
            right_arm = max(0, traverse(root.right))

            self.max_sum = max(root.val + right_arm + left_arm, self.max_sum)

            return root.val + max(left_arm, right_arm)

        traverse(root)

        return self.max_sum
