class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        adj_mapping = defaultdict(list)
        count = {}

        for a, b, c in edges:
            adj_mapping[a].append((b, c))
            adj_mapping[b].append((a, c))

        for i in range(n):
            dist_heap = []
            visited = set()

            dist_heap.append((0, i))

            while dist_heap:
                cur_dist, node = heapq.heappop(dist_heap)

                if cur_dist > distanceThreshold:
                    continue

                if node in visited:
                    continue

                visited.add(node)
                count[i] = count.get(i, 0) + 1

                for neighbor, c in adj_mapping[node]:
                    heapq.heappush(dist_heap, (cur_dist + c, neighbor))

        min_count = min(count.values())
        for key in sorted(count.keys(), reverse=True):
            if count[key] == min_count:
                return key