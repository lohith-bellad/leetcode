# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        def traverse(rootA, rootB):
            if (not rootA and rootB) or (rootA and not rootB):
                return False

            if not rootA and not rootB:
                return True

            if rootA.val != rootB.val:
                return False

            return (traverse(rootA.left, rootB.right) and
                    traverse(rootA.right, rootB.left))

        if not root:
            return True
        
        return traverse(root.left, root.right)
        """
        queue = deque()
        queue.append((root, root))

        while queue:
            rootA, rootB = queue.popleft()

            if (not rootA and rootB) or (rootA and not rootB):
                return False

            if not rootA and not rootB:
                continue

            if rootA.val != rootB.val:
                return False
            
            queue.append((rootA.left, rootB.right))
            queue.append((rootA.right, rootB.left))

        return True