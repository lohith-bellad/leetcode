class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        minHeap = []
        max_rooms = 1
        intervals.sort()

        heapq.heappush(minHeap, intervals[0][1])

        for i in range(1, len(intervals)):
            if minHeap[0] <= intervals[i][0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i][1])

            max_rooms = max(max_rooms, len(minHeap))

        return max_rooms
        """
        intervals.sort()
        min_heap = []
        output = 0

        for interval in intervals:
            if not min_heap:
                heapq.heappush(min_heap, interval[1])

            else:
                if min_heap[0] <= interval[0]:
                    heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval[1])

            output = max(output, len(min_heap))
        
        return output