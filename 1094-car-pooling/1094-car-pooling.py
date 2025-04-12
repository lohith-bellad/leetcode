class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
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
        """
        my_stack = []

        for pass_count, start, end in trips:
            my_stack.append((start, pass_count))
            my_stack.append((end, -pass_count))

        my_stack.sort()

        cur_count = 0
        for stamp, count in my_stack:
            cur_count += count
            if cur_count > capacity:
                return False

        return True