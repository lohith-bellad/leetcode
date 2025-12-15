# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = defaultdict(list)
        queue = deque()
        queue.append((root, 0, 0))

        while len(queue) > 0:
            for i in range(len(queue)):
                node, row, col = queue.popleft()

                mapping[col].append((row, node.val))

                if node.left:
                    queue.append((node.left, row + 1, col - 1))

                if node.right:
                    queue.append((node.right, row + 1, col + 1))

        output = []
        for cols in sorted(mapping.keys()):
            temp = []
            for n in sorted(mapping[cols]):
                temp.append(n[1])
            output.append(temp)

        return output
