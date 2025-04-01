# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root: TreeNode, num: int) -> bool:
            if root == None:
                return True
            
            left = traverse(root.left, num)
            if root.val <= num:
                return False
            right = traverse(root.right, root.val)

            return left and right

        return traverse(root, float('-inf'))

