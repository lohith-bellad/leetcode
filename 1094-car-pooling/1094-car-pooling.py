class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0 for i in range(1000)]

        for trip in trips:
            c, start, end = trip
            for i in range(start, end):
                path[i] += c
                if path[i] > capacity:
                    return False
        
        return True