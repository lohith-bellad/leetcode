# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        def range_sum(root: TreeNode, low: int, high: int) -> int:
            if root == None:
                return 0
    
            if low <= root.val <= high:
                return root.val + range_sum(root.left, low, high) + range_sum(root.right, low, high)
    
            if root.val < low:
                return range_sum(root.right, low, high)
    
            if root.val > high:
                return range_sum(root.left, low, high)

        return range_sum(root, low, high)

        def traverse(root, low, high):
            if not root:
                return

            if low <= root.val <= high:
                self.range_sum += root.val
                traverse(root.left, low, high)
                traverse(root.right, low, high)
            elif root.val < low:
                traverse(root.right, low, high)
            elif root.val > high:
                traverse(root.left, low, high)

            return

        self.range_sum = 0
        traverse(root, low, high)

        return self.range_sum
        """
        def traverse(root, low, high, cur_val):
            if not root:
                return cur_val
            
            left = traverse(root.left, low, high, cur_val)
            right = traverse(root.right, low, high, cur_val)

            val = left + right
            if low <= root.val <= high:
                val += root.val
            
            return val
        
        return traverse(root, low, high, 0)