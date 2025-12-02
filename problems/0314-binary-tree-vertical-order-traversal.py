"""
314. Binary Tree Vertical Order Traversal
Medium

Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.


Example 1:
    Input: root = [3,9,20,null,null,15,7]
           3
          / \
         9  20
            / \
           15  7
    Output: [[9],[3,15],[20],[7]]

Example 2:
    Input: root = [3,9,8,4,0,1,7]
             3
            / \
           9   8
          / \ / \
         4  0 1  7
    Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
    Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
     (0's right child is 2 and 1's left child is 5)
             3
            / \
           9   8
          / \ / \
         4  0 1  7
            / \
           5   2
    Output: [[4],[9,5],[3,0,1],[8,2],[7]]


Constraints:
    * The number of nodes in the tree is in the range [0, 100]
    * -100 <= Node.val <= 100

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        hmap = defaultdict(list)

        while queue:
            node, ind = queue.popleft()
            hmap[ind].append(node.val)

            if node.left:
                queue.append((node.left, ind - 1))

            if node.right:
                queue.append((node.right, ind + 1))

        sorted_keys = sorted(hmap.keys())
        output = []

        for key in sorted_keys:
            output.append(hmap[key])

        return output
