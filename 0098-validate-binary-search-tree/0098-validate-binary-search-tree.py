# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root: TreeNode, arr: []):
            if root == None:
                return
            
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)

            return

        inp = []
        traverse(root, inp)

        for i in range(len(inp) - 1):
            if inp[i] >= inp[i + 1]:
                return False
        
        return True

