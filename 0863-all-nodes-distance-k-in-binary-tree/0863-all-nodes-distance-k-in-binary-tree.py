# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: 
        """
        adj_list = defaultdict(list)

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if node.left != None:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)
                queue.append(node.left)

            if node.right != None:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
                queue.append(node.right)
        
        depth = 0
        visited = set()
        queue = deque()
        queue.append(target.val)
        visited.add(target.val)

        while len(queue) > 0:
            if depth == k:
                break

            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                neighbors = adj_list[node]
                for n in neighbors:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)

        output = []
        while len(queue) > 0:
            output.append(queue.popleft())
        
        return output
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