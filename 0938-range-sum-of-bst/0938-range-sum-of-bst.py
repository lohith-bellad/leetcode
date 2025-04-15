# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        def traverse(root: TreeNode, low: int, high: int):
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


        traverse(root, low, high)
        return self.total
