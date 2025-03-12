# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def traverse(root: TreeNode, levels: [], ind: int):
            if root == None:
                return

            if len(levels) == ind:
                levels.append(0)

            levels[ind] = root.val

            traverse(root.left, levels, ind + 1)
            traverse(root.right, levels, ind + 1)
            return
        
        traverse(root, levels, 0)

        return levels