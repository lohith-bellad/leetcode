# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: 
        """
        def dfs(node: int, visited: {}, depth: int):
            if node in visited:
                return

            if depth == k:
                self.output.append(node)

            visited.add(node)

            for neighbor in adj_map[node]:
                dfs(neighbor, visited, depth + 1)

            return
    
        if k == 0:
            return [target.val]

        self.output = []
        adj_map = defaultdict(list)
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left != None:
                adj_map[node.val].append(node.left.val)
                adj_map[node.left.val].append(node.val)
                queue.append(node.left)

            if node.right != None:
                adj_map[node.val].append(node.right.val)
                adj_map[node.right.val].append(node.val)
                queue.append(node.right)

        depth = 1
        visited = set()
        visited.add(target.val)
        for neighbor in adj_map[target.val]:
            dfs(neighbor, visited, depth)

        return self.output
        """
        def dfs(cur_node, dist):
            if dist == k:
                self.output.append(cur_node)
            
            if dist > k:
                return
            
            self.visited.add(cur_node)
            
            for neighbor in nodeMap[cur_node]:
                if neighbor not in self.visited:
                    dfs(neighbor, dist + 1)
            
            return

        nodeMap = defaultdict(list)
        queue = deque()
        queue.append(root)

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
        self.output = []

        dfs(target.val, 0)
        return self.output