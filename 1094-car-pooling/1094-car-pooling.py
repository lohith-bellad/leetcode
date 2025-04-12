class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        max_dist = trips[-1][2]
        path = [0 for i in range(max_dist)]

        for trip in trips:
            c, start, end = trip
            for i in range(start, end):
                path[i] += c
                if path[i] > capacity:
                    return False
        
        return True