# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def traverse(inorder: List[int], postorder: List[int]) -> TreeNode:
            if len(inorder) == 0 or len(postorder) == 0:
                return None
            
            root = TreeNode(postorder.pop())
            mid = inorder.index(root.val)

            root.right = traverse(inorder[mid + 1:], postorder)
            root.left = traverse(inorder[:mid], postorder)

            return root
        
        return traverse(inorder, postorder)