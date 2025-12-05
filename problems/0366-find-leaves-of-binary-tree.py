"""
366. Find Leaves of Binary Tree
Medium

Given the root of a binary tree, collect a tree's nodes as if you were doing this:
    1. Collect all the leaf nodes.
    2. Remove all the leaf nodes.
    3. Repeat until the tree is empty.


Example 1:
    Input: root = [1,2,3,4,5]
          1
         / \
        2   3
       / \
      4   5

    Output: [[4,5,3],[2],[1]]
    Explanation:
        [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers
        since per each level it does not matter the order on which elements are returned.


Constraints:
    * The number of nodes in the tree is in the range [1, 100].
    * -100 <= Node.val <= 100

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root):
            if not root:
                return None

            # Leaf node
            if not root.left and not root.right:
                self.output[-1].append(root.val)
                return None

            root.left = traverse(root.left)
            root.right = traverse(root.right)

            return root

        self.output = []
        while root:
            self.output.append([])
            root = traverse(root)

        return self.output
