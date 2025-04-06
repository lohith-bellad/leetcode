# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root: TreeNode) -> TreeNode:
            if root == None:
                return None

            root.left = traverse(root.left)
            root.right = traverse(root.right)

            if not root.left and not root.right:
                if root.val == 1:
                    return root
                else:
                    return None
            return root
        
        return traverse(root)