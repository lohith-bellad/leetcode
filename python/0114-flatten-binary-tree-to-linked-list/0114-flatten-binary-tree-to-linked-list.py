# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(root: TreeNode) -> TreeNode:
            if root == None:
                return None
            
            if root.left == None and root.right == None:
                return root
            
            left_hand = traverse(root.left)
            right_hand = traverse(root.right)

            if left_hand != None:
                left_hand.right = root.right
                root.right = root.left
                root.left = None
            
            if right_hand != None:
                return right_hand
            return left_hand
        
        traverse(root)
        return