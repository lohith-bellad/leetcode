# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        self.current = -1

        def traverse(root: TreeNode):
            if root == None:
                return

            traverse(root.left)
            self.list.append(root.val)
            traverse(root.right)

        traverse(root)

    def next(self) -> int:
        self.current += 1
        return self.list[self.current]

    def hasNext(self) -> bool:
        if self.current + 1 < len(self.list):
            return True

        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
