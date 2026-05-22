# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def find_total_sum(root):
            if not root:
                return 0

            left = find_total_sum(root.left)
            right = find_total_sum(root.right)

            return root.val + left + right
        
        def traverse(root):
            if not root:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)

            cur_sum = root.val + left + right
            self.max_prod = max(self.max_prod, (self.total_sum - cur_sum) * cur_sum)

            return cur_sum

        self.total_sum = find_total_sum(root)
        self.max_prod = 0
        traverse(root)

        return self.max_prod % (10**9 + 7)
