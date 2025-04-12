class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_dist = 0
        for trip in trips:
            max_dist = max(max_dist, trip[2])

        path = [0 for i in range(max_dist + 1)]

        for trip in trips:
            c, start, end = trip
            for i in range(start, end):
                path[i] += c
                if path[i] > capacity:
                    return False
        
        return True