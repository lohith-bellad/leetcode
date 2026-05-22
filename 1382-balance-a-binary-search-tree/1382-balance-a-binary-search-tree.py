# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            self.nums.append(root.val)
            traverse(root.right)
        
        def build_tree(start, end):
            if start > end:
                return None

            mid = start + (end - start) // 2

            new_node = TreeNode(self.nums[mid])
            new_node.left = build_tree(start, mid - 1)
            new_node.right = build_tree(mid + 1, end)
            return new_node
        
        self.nums = []
        traverse(root)
        return build_tree(0, len(self.nums) - 1)