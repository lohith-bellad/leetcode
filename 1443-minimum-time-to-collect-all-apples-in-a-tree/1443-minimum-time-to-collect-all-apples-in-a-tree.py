class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(level: int):
            if level in visited:
                return 0

            visited.add(level)
            steps = 0
            total = 0
            for neighbors in node_map[level]:
                steps += dfs(neighbors)
            
            if steps or hasApple[level]:
                total += 2 + steps
            
            return total

        ind = 0
        while ind < len(hasApple) and hasApple[ind] == False:
            ind += 1
        
        if ind == len(hasApple):
            return 0
        
        node_map = defaultdict(list)

        for l, r in edges:
            node_map[l].append(r)
            node_map[r].append(l)
        
        visited = set()
        return dfs(0) - 2