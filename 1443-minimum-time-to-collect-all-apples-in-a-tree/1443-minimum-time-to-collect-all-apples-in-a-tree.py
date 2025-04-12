class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(level: int):
            print(f"level={level}")
            steps = 0
            total = 0
            for neighbors in node_map[level]:
                steps += dfs(neighbors)
            
            if steps or hasApple[level]:
                total += 2 + steps
            
            print(total)
            return total

        node_map = defaultdict(list)

        for l, r in edges:
            node_map[l].append(r)
        
        tot = dfs(0)
        if tot > 0:
            return tot - 2
        return tot