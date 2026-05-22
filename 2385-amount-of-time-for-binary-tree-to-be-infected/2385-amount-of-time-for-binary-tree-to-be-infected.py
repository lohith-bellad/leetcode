# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node, depth):
            if node in self.visited:
                return
            
            self.visited.add(node)
            self.max_time = max(self.max_time, depth)

            for neighbor in nodeMap[node]:
                dfs(neighbor, depth + 1)
            
            return

        queue = deque()
        queue.append(root)
        nodeMap = defaultdict(list)

        while queue:
            node = queue.popleft()

            if node.left:
                nodeMap[node.val].append(node.left.val)
                nodeMap[node.left.val].append(node.val)
                queue.append(node.left)
            
            if node.right:
                nodeMap[node.val].append(node.right.val)
                nodeMap[node.right.val].append(node.val)
                queue.append(node.right)

        self.max_time = 0
        self.visited = set()
        dfs(start, 0)

        return self.max_time