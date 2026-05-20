# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        def traverse(root):
            if not root:
                return None
            
            # Leaf node
            if not root.left and not root.right:
                self.output[-1].append(root.val)
                return None
            
            root.left = traverse(root.left)
            root.right = traverse(root.right)

            return root

        self.output = []
        while root:
            self.output.append([])
            root = traverse(root)
        
        return self.output
        """
        def traverse(root):
            if not root:
                return None
            
            if not root.left and not root.right:
                self.levels[-1].append(root.val)
                return None
            
            root.left = traverse(root.left)
            root.right = traverse(root.right)

            return root
        
        self.levels = []
        while root:
            self.levels.append([])
            root = traverse(root)

        return self.levels