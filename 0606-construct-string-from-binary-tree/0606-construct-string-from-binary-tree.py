# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(root: TreeNode, s: []):
            if root == None:
                s.append("")
                return
            
            s.append(str(root.val))
            s.append("(")
            if root.left == None and root.right == None:
                s.pop()
            else:
                traverse(root.left, s)
                s.append(")")
            s.append("(")
            if root.right == None:
                s.pop()
            else:
                traverse(root.right, s)
                s.append(")")

            return
        
        output = []
        traverse(root, output)
        return "".join(output)