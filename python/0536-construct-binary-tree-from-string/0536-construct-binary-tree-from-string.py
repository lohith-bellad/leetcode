# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def traverse(s, ind: int) -> TreeNode:
            end = ind
            while end < len(s) and (s[end].isdigit() or s[end] == "-"):
                end += 1

            value = int(s[ind:end])
            new_node = TreeNode(value)

            if end < len(s) and s[end] == "(":
                new_node.left, end = traverse(s, end + 1)

            if end < len(s) and s[end] == "(":
                new_node.right, end = traverse(s, end + 1)

            return new_node, end + 1

        if len(s) == 0:
            return None

        root, i = traverse(s, 0)
        return root
