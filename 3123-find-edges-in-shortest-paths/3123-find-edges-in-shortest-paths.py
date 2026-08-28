class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        def find_shortest_dist(node):
            distances = {}
            min_heap = [(0, node)]

            while min_heap:
                dist, cur_node = heapq.heappop(min_heap)

                if cur_node in distances:
                    continue
                distances[cur_node] = dist

                for neighbor, w in mapping[cur_node]:
                    if neighbor not in distances:
                        heapq.heappush(min_heap, (w + dist, neighbor))

            return distances

        mapping = defaultdict(list)
        for s, d, w in edges:
            mapping[s].append((d, w))
            mapping[d].append((s, w))

        dist_from_src = find_shortest_dist(0)
        dist_from_dst = find_shortest_dist(n - 1)

        output = [False for _ in range(len(edges))]

        if (n - 1) not in dist_from_src:
            return output

        min_dist = dist_from_src[n - 1]

        for i, (u, v, w) in enumerate(edges):
            if u in dist_from_src and v in dist_from_dst:
                if dist_from_src[u] + w + dist_from_dst[v] == min_dist:
                    output[i] = True
                    continue
            if v in dist_from_src and u in dist_from_dst:
                if dist_from_src[v] + w + dist_from_dst[u] == min_dist:
                    output[i] = True

        return output
                
            
            