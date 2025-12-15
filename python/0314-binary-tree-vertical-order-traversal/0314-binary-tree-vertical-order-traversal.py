# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_map = {}
        queue = deque()
        output = []
        queue.append((root, 0))

        while len(queue) > 0:
            node, ind = queue.popleft()

            if node is None:
                continue

            if ind not in hash_map:
                hash_map[ind] = []
            hash_map[ind].append(node.val)

            if node.left is not None:
                queue.append((node.left, ind - 1))

            if node.right is not None:
                queue.append((node.right, ind + 1))

        sorted_keys = sorted(hash_map.keys())

        for key in sorted_keys:
            output.append(hash_map[key])

        return output
