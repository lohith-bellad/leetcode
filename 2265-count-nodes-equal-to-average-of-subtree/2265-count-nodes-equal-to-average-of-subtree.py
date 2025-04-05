# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def traverse(root: TreeNode):
            if root == None:
                return 0, 0

            left_sum = right_sum = 0
            left_mem = right_mem = 0

            if root.left:
                left_sum, left_mem = traverse(root.left)
            
            if root.right:
                right_sum, right_mem = traverse(root.right)

            total = left_sum + right_sum + root.val
            mem_total = 1 + left_mem + right_mem
            avg = total // mem_total

            if avg == root.val:
                self.count += 1
            
            return total, mem_total
        
        traverse(root)
        return self.count