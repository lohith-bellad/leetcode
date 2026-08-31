# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        def traverse(r1, r2):
            if not r1 and not r2:
                return None
            
            new_node = TreeNode(0)

            if r1 and r2:
                new_node.val = r1.val + r2.val
                new_node.left = traverse(r1.left, r2.left)
                new_node.right = traverse(r1.right, r2.right)
            elif r1:
                new_node.val = r1.val
                new_node.left = traverse(r1.left, None)
                new_node.right = traverse(r1.right, None)
            elif r2:
                new_node.val = r2.val
                new_node.left = traverse(None, r2.left)
                new_node.right = traverse(None, r2.right)
            
            return new_node
        
        return traverse(root1, root2)
        """
        if not root1 or not root2:
            if not root1:
                return root2
            return root1

        val = root1.val + root2.val
        new_node = TreeNode(val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)

        return new_node