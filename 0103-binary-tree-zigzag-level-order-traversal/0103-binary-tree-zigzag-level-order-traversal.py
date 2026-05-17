# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root, ind):
            if not root:
                return
            
            if len(self.levels) == ind:
                self.levels.append([])
            
            self.levels[ind].append(root.val)

            traverse(root.left, ind + 1)
            traverse(root.right, ind + 1)
        
        self.levels = []
        traverse(root, 0)

        for i in range(len(self.levels)):
            if i % 2 == 1:
                self.levels[i].reverse()
        
        return self.levels