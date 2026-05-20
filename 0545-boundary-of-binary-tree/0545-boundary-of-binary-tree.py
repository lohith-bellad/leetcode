# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def left_boundary(root):
            if not root:
                return
            
            if root.left:
                self.output.append(root.val)
                left_boundary(root.left)
            elif root.right:
                self.output.append(root.val)
                left_boundary(root.right)
            return
        
        def right_boundary(root):
            if not root:
                return
            
            if root.right:
                right_boundary(root.right)
                self.output.append(root.val)
            elif root.left:
                right_boundary(root.left)
                self.output.append(root.val)
            return
        
        def bottom_boundary(root):
            if root == None:
                return
            
            if root.right == None and root.left == None:
                self.output.append(root.val)
            
            bottom_boundary(root.left)
            bottom_boundary(root.right)
            return
        
        self.output = []
        if root == None:
            return self.output
        
        self.output.append(root.val)
        if not root.left and not root.right:
            return self.output
            
        left_boundary(root.left)
        bottom_boundary(root)
        right_boundary(root.right)

        return self.output