"""
1161. Maximum Level Sum of a Binary Tree
Medium

Given the root of a binary tree, the level of its root is 1, the level of its
children is 2, and so on.

Return the smallest level x such that the sum of all the nodes at level x is
maximal.


Example 1:
    Input: root = [1,7,0,7,-8,null,null]
    Output: 2
    Explanation:
        Level 1 sum = 1.
        Level 2 sum = 7 + 0 = 7.
        Level 3 sum = 7 + (-8) = -1.
        So we return the level with the maximum sum which is level 2.

Example 2:
    Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    Output: 2


Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * -10^5 <= Node.val <= 10^5

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def traverse(root, ind):
            if not root:
                return

            if len(self.level_sum) == ind:
                self.level_sum.append(0)

            self.level_sum[ind] += root.val

            traverse(root.left, ind + 1)
            traverse(root.right, ind + 1)

        self.level_sum = []
        traverse(root, 0)

        max_sum = max(self.level_sum)

        for ind in range(len(self.level_sum)):
            if self.level_sum[ind] == max_sum:
                return ind + 1

        return -1
