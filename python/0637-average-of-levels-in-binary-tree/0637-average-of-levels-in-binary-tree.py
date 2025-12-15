# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.levels = []

        def traverse(root: TreeNode, levels: [], ind: int):
            if root == None:
                return

            if len(levels) == ind:
                levels.append((0, 0))

            total, cnt = levels[ind]
            total += root.val
            cnt += 1
            levels[ind] = (total, cnt)

            traverse(root.left, levels, ind + 1)
            traverse(root.right, levels, ind + 1)

        traverse(root, self.levels, 0)
        output = []
        for total, cnt in self.levels:
            avg = (total * 1.0) / cnt
            output.append(avg)

        return output
