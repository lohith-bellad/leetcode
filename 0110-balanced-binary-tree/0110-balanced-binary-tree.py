# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        def traverse(root: TreeNode) -> (bool, int):
            if root == None:
                return (True, 0)
            
            left_balanced, left_height = traverse(root.left)
            right_balanced, right_height = traverse(root.right)

            if left_balanced == False or right_balanced == False or abs(left_height - right_height) > 1:
                return (False, 0)
            
            return (True, max(left_height, right_height) + 1)

        balanced, height = traverse(root)
        return balanced
        """
        def traverse(root) -> (bool, int):
            if not root:
                return True, 0
            
            left_balanced, left_depth = traverse(root.left)
            right_balanced, right_depth = traverse(root.right)

            if not left_balanced or not right_balanced or abs(left_depth - right_depth) > 1:
                return False, 0
            
            return True, max(left_depth, right_depth) + 1
    
        return traverse(root)[0]
            
