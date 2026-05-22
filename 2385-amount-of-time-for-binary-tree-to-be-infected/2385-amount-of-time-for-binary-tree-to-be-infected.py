# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node in self.visited:
                return 0
            
            self.visited.add(node)

            cur_max = 0
            for neighbor in nodeMap[node]:
                if neighbor not in self.visited:
                    cur_max = max(cur_max, dfs(neighbor) + 1)
            
            return cur_max

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

        self.visited = set()
        return dfs(start)