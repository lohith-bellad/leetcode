# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        def traverse(root: TreeNode) -> bool:
            if root == None:
                return True
            
            if not traverse(root.left):
                return False

            if root.val <= self.num:
                return False
            
            self.num = root.val
 
            return traverse(root.right)

        self.num = float('-inf')
        return traverse(root)
        """
        def traverse(root: TreeNode, arr: []):
            if root == None:
                return True
            
            left = traverse(root.left, arr)

            if len(arr) > 0 and arr[-1] >= root.val:
                return False
            else:
                arr.append(root.val)
            
            right = traverse(root.right, arr)

            return left and right

        return traverse(root, [])