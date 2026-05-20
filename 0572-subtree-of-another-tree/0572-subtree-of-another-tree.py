# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        def same_tree(root1: TreeNode, root2: TreeNode) -> bool:
            if (not root1 and root2) or (root1 and not root2):
                return False
            if not root1 and not root2:
                return True
            if root1.val != root2.val:
                return False

            return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

        def traverse(root1: TreeNode, root2: TreeNode) -> bool:
            if root1 == None:
                return False
            
            if root1.val == root2.val and same_tree(root1, root2):
                return True
            
            return traverse(root1.left, root2) or traverse(root1.right, root2)

        return traverse(root, subRoot)    
        """
        def sameTree(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            
            return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)
        
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    