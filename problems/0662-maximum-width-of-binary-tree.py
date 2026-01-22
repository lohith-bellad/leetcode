"""
662. Maximum Width of Binary Tree
Medium

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the
leftmost and rightmost non-null nodes), where the null nodes between the
end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.


Example 1:
    Input: root = [1,3,2,5,3,null,9]
    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:
    Input: root = [1,3,null,5,3]
    Output: 2
    Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
    Input: root = [1,3,2,5]
    Output: 2
    Explanation: The maximum width existing in the second level with the length 2 (3,2).


Constraints:
    * The number of nodes in the tree is in the range [1, 3000].
    * -100 <= Node.val <= 100

"""

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append((root, 0))
        max_width = 0

        while queue:
            first_col_ind = queue[0][1]
            last_col_ind = -1

            for _ in range(len(queue)):
                cur_node, col_ind = queue.popleft()
                last_col_ind = col_ind

                if cur_node.left:
                    queue.append((cur_node.left, 2 * col_ind))

                if cur_node.right:
                    queue.append((cur_node.right, 2 * col_ind + 1))

            max_width = max(max_width, last_col_ind - first_col_ind + 1)

        return max_width
