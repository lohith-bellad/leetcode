class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def manhattan_dist(x, y, p, q):
            return abs(x - p) + abs(y - q)
        
        st_x, st_y = start
        t_x, t_y = target
        min_heap = [(0, st_x, st_y)]
        dist_map = {(st_x, st_y): 0}
        output = manhattan_dist(st_x, st_y, t_x, t_y)

        while min_heap:
            dist, cur_x, cur_y = heapq.heappop(min_heap)
            
            output = min(output, dist + manhattan_dist(cur_x, cur_y, t_x, t_y))

            for x1, y1, x2, y2, w in specialRoads:
                ndist = dist + manhattan_dist(cur_x, cur_y, x1, y1) + w
                if ndist < dist_map.get((x2, y2), float("inf")):
                    dist_map[(x2, y2)] = ndist
                    heapq.heappush(min_heap, (ndist, x2, y2))
        
        return output
