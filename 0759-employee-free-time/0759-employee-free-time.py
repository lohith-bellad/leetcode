"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        minHeap = []
        output = []
        busy = []

        for employee in schedule:
            for interval in employee:
                heapq.heappush(minHeap, (interval.start, interval.end))
        
        while minHeap:
            x, y = heapq.heappop(minHeap)
            if not busy:
                busy.append([x, y])
            else:
                last_x, last_y = busy[-1]
                if x <= last_y:
                    busy[-1][1] = max(y, last_y)
                else:
                    output.append(Interval(last_y, x))
                    busy.append([x, y])

        return output