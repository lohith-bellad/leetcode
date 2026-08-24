class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        holes = []
        start = 0

        for i in range(len(startTime)):
            gap = startTime[i] - start
            holes.append(gap)
            start = endTime[i]

        holes.append(eventTime - start)
        print(holes)

        win_size = min(k + 1, len(holes))
        free_time = sum(holes[:win_size])
        max_free_time = free_time

        for i in range(win_size, len(holes)):
            free_time += holes[i] - holes[i - win_size]
            max_free_time = max(free_time, max_free_time)

        return max_free_time