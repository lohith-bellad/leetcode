# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        self.ind = 0
        def traverse(root: TreeNode, k: int) -> TreeNode:
            if root == None:
                return None
            
            left_hand = traverse(root.left, k)
            if left_hand != None:
                return left_hand
            self.ind += 1
            if self.ind == k:
                return root

            return traverse(root.right, k)
        
        output = traverse(root, k)
        
        if output != None:
            return output.val
        return 0
        """
        def traverse(root):
            if not root:
                return
            
            if self.smallest != float("inf"):
                return
            
            traverse(root.left)
            self.count += 1
            if self.count == k:
                self.smallest = root.val
            traverse(root.right)

            return
        self.count = 0
        self.smallest = float("inf")
        traverse(root)

        return self.smallest