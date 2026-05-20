# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def left_traverse(root):
            if not root:
                return
            
            if root.left or root.right:
                self.output.append(root.val)
            
            if root.left:
                left_traverse(root.left)
            elif root.right:
                left_traverse(root.right)
            
            return
        
        def right_traverse(root):
            if not root:
                return
            
            if root.right:
                right_traverse(root.right)
            elif root.left:
                right_traverse(root.left)
            
            if root.left or root.right:
                 self.output.append(root.val)
                 
            return
        
        def bottom_traverse(root):
            if not root:
                return
            
            if not root.left and not root.right:
                self.output.append(root.val)
                return
            
            if root.left:
                bottom_traverse(root.left)
            
            if root.right:
                bottom_traverse(root.right)
            return
        
        self.output = []

        self.output.append(root.val)
        if not root.left and not root.right:
            return self.output
        
        left_traverse(root.left)
        bottom_traverse(root)
        right_traverse(root.right)

        return self.output