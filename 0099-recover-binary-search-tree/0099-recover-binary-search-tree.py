# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.a = None
        self.b = None

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)

            if self.prev and self.prev.val > root.val:
                if not self.a:
                    self.a = self.prev
                self.b = root
            
            self.prev = root

            dfs(root.right)
        
        dfs(root)
        if self.a and self.b:
            self.a.val, self.b.val = self.b.val, self.a.val