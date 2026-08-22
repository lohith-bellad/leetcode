class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        intervals.sort()
        myStack = []

        myStack.append(intervals[0])

        for i in range(1, len(intervals)):
            last_x, last_y = myStack[-1]
            cur_x, cur_y = intervals[i]

            if last_x <= cur_x <= last_y:
                myStack[-1][1] = max(last_y, cur_y)
            else:
                myStack.append(intervals[i])
        
        return myStack
        """
        intervals.sort()
        my_stack = []

        for interval in intervals:
            if not my_stack:
                my_stack.append(interval)
            else:
                last_start, last_end = my_stack[-1]
                cur_start, cur_end = interval

                if last_start <= cur_start <= last_end:
                    my_stack[-1] = [last_start, max(cur_end, last_end)]
                else:
                    my_stack.append(interval)

        return my_stack