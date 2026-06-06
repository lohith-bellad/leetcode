class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        if len(intervals) < 2:
            return True

        intervals.sort(key = lambda x: x[0])

        prev_start, prev_end = intervals[0]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]

            if prev_start <= cur_start < prev_end:
                return False
            
            prev_start, prev_end = cur_start, cur_end
        
        return True
        """
        if not intervals:
            return True
        
        intervals.sort()
        ind = 1
        while ind < len(intervals):
            prev_x, prev_y = intervals[ind - 1]
            cur_x, cur_y = intervals[ind]

            if prev_x <= cur_x < prev_y:
                return False
            
            ind += 1
        
        return True