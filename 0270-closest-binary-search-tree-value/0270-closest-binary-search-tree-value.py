# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        def traverse(root: TreeNode, target: int) -> int:
            if root == None:
                return float('inf')
            
            if root.val > target:
                l = traverse(root.left, target)
                return min(l, root.val, key = lambda x: (abs(target - x), x))
            else:
                r = traverse(root.right, target)
                return min(r, root.val, key = lambda x: (abs(target - x), x))
            
        return traverse(root, target)
        """
        closet_seen = float('inf')
        res = 0

        while root:
            diff = abs(root.val - target)
            if diff < closet_seen or (diff == closet_seen and root.val < res):
                closet_seen = diff
                res = root.val
        
            if root.val > target:
                root = root.left
            else:
                root = root.right
    
        return res