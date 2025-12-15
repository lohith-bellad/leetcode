class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        my_stack = []
        output = [0 for i in range(n)]

        for log in logs:
            tid, action, ttime = log.split(":")
            tid = int(tid)
            ttime = int(ttime)

            if action == "start":
                my_stack.append([tid, ttime, 0])

            else:
                tid, start_time, otime = my_stack.pop()
                duration = ttime - start_time + 1 - otime
                if len(my_stack) > 0:
                    my_stack[-1][2] += duration + otime
                output[tid] += duration

        return output
