# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        queue = deque([root])

        while queue[0] != None:
            node = queue.popleft()
            queue.append(node.left)
            queue.append(node.right)

        while len(queue) > 0 and queue[0] == None:
            queue.popleft()

        if len(queue) > 0:
            return False

        return True
