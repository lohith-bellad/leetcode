# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeMap = defaultdict(list)
        queue = deque()
        queue.append((0, 0, root))

        while queue:
            row, col, node = queue.popleft()

            nodeMap[col].append((row, node.val))

            if node.left:
                queue.append((row + 1, col - 1, node.left))
            
            if node.right:
                queue.append((row + 1, col + 1, node.right))
        
        output = []
        sorted_keys = sorted(nodeMap.keys())

        for key in sorted_keys:
            vals = sorted(nodeMap[key])
            temp = []
            for val in vals:
                temp.append(val[1])
            output.append(temp)
        
        return output