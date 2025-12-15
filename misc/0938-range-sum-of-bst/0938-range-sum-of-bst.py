# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0

        def range_sum(root: TreeNode, low: int, high: int) -> int:
            if root == None:
                return 0

            if low <= root.val <= high:
                return (
                    root.val
                    + range_sum(root.left, low, high)
                    + range_sum(root.right, low, high)
                )

            if root.val < low:
                return range_sum(root.right, low, high)

            if root.val > high:
                return range_sum(root.left, low, high)
            """
            if root == None:
                return
            
            if low <= root.val <= high:
                self.total += root.val
                traverse(root.left, low, high)
                traverse(root.right, low, high)
            elif root.val < low:
                traverse(root.right, low, high)
            else:
                traverse(root.left, low, high)
            """

        return range_sum(root, low, high)
        # return self.total
