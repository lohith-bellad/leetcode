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
        """
        def traverse(root, leaves):
            if not root:
                return None

            if not root.left and not root.right:
                leaves.append(root.val)
                return None
            
            root.left = traverse(root.left, leaves)
            root.right = traverse(root.right, leaves)

            return root

        output = []
        while root:
            leaves = []
            root = traverse(root, leaves)
            output.append(leaves)

        return output