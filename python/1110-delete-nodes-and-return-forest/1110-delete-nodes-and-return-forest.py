# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def traverse(root: TreeNode, to_delete: []) -> TreeNode:
            if root == None:
                return None

            root.left = traverse(root.left, to_delete)
            root.right = traverse(root.right, to_delete)

            if root.val in to_delete:
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)
                return None
                
            return root

        forest = []
        root = traverse(root, to_delete)
        if root:
            forest.append(root)

        return forest