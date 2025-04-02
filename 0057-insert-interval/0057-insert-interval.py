class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        ind = 0

        if len(intervals) == 0:
            return [newInterval]

        while ind < len(intervals) and intervals[ind][1] < newInterval[0]:
            output.append(intervals[ind])
            ind += 1
        
        while ind < len(intervals) and intervals[ind][0] <= newInterval[1]:
            newInterval[0] = min(intervals[ind][0], newInterval[0])
            newInterval[1] = max(intervals[ind][1], newInterval[1])
            ind += 1
        output.append(newInterval)
        
        while ind < len(intervals):
            output.append(intervals[ind])
            ind += 1
        
        return output