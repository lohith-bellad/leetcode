class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        my_stack = []

        for interval in intervals:
            if not my_stack:
                my_stack.append(interval)
            else:
                last_x, last_y = my_stack[-1]
                new_x, new_y = interval

                if last_x <= new_x and new_y <= last_y:
                    continue
                
                if last_x == new_x and new_y > last_y:
                    my_stack[-1][1] = new_y
                    continue
                    
                my_stack.append(interval)
        
        return len(my_stack)