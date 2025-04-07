# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []
        def traverse(root: TreeNode, ind: int, levels: []):
            if root == None:
                return

            if len(levels) == ind:
                levels.append([])
            
            levels[ind].append(root.val)

            traverse(root.left, ind + 1, levels)
            traverse(root.right, ind + 1, levels)
        
        traverse(root, 0, self.levels)

        for i in range(1, len(self.levels), 2):
            self.levels[i].reverse()
        
        return self.levels