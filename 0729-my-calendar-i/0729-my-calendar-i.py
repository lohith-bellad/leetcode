class MyCalendar:
    def __init__(self):
        self.reserved_slots = []

    def book(self, startTime: int, endTime: int) -> bool:
        start = 0
        end = len(self.reserved_slots) - 1

        while start <= end:
            mid = start + (end - start) // 2
            cur_start, cur_end = self.reserved_slots[mid]

            if startTime < cur_end and endTime > cur_start:
                return False

            if endTime <= cur_start:
                end = mid - 1
            else:
                start = mid + 1

        self.reserved_slots.append([startTime, endTime])
        self.reserved_slots.sort()
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)