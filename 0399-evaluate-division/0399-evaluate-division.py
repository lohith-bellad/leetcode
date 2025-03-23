class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        output = []

        def findPair(graph: {}, p: str, q: str, path: [], prod: float) -> float:
            if p in path:
                return -1.0

            for link, cost in graph[p]:
                if link == q:
                    return prod*cost
                else:
                    path.append(p)
                    c = findPair(graph, link, q, path, prod*cost)
                    if c != -1:
                        return c
            
            return -1

        ind = 0
        for a, b in equations:
            if a not in graph:
                graph[a] = []
            graph[a].append((b, values[ind]))
            if b not in graph:
                graph[b] = []
            graph[b].append((a, 1 / values[ind]))
            ind += 1
        
        for p, q in queries:
            if p not in graph or q not in graph:
                output.append(-1.0)
            elif p == q:
                output.append(1.0)
            else:
                output.append(findPair(graph, p, q, [], 1))

        return output